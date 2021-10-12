import os
import random
import torch
import tensorflow as tf
import numpy as np
from ktrain import text, get_predictor, get_learner


# to ensure as much reproducibility as possible we set all python and package seeds
# BERT results still vary form run to run with fixed seeds and parameters due to internal segmentation
def set_seeds(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


# train function takes training texts, training labels, validation texts, and validation labels
# STRONGLY RECOMMNED adding a checkpoint folder by setting checkpoint_folder, e.g.:
# .., checkpoint_folder="D:/Hubert/checkpoint/"
# this will save the parameters of each epoch. We can load the best one after training has finished
def train_learner(X_train, y_train, X_val, y_val,
                  lr, epoch, seed, text_length, checkpoint_folder=None, model_name="bert-base-uncased"):
    classNames = y_train.unique()

    set_seeds(seed)

    t = text.Transformer(model_name, maxlen=text_length, class_names=classNames)
    trn = t.preprocess_train(X_train, y_train)
    val = t.preprocess_test(X_val, y_val)
    model2 = t.get_classifier()
    learner = get_learner(model2, train_data=trn, val_data=val, batch_size=32)
    # learner.lr_find(max_epochs=5)
    learner.fit_onecycle(lr, epoch, checkpoint_folder=checkpoint_folder)
    return learner, t, trn, val, model2
    # return learner.lr_plot()


# function that uses a trained model and predicts on test set
def predict_test(x_test, learner, t, trn):
    predictor = get_predictor(learner.model, preproc=t)
    pred = predictor.predict(x_test)
    return np.squeeze(pred), predictor
