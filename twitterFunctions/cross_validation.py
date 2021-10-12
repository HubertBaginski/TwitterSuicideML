import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import make_scorer, precision_score, f1_score, accuracy_score, recall_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


def run_SVM_CV(train_features, test_features, y_train, y_test, confusion=True, verbose=True):
    metrics = np.zeros(4)

    pipeline = Pipeline([
        ('vect', TfidfVectorizer()),
        ('clf', SVC(random_state=1)),
    ])

    # here we can play around with the parameters
    # for SVM params check https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    # for tfidf params check https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

    parameters = {
        #  'vect__max_df': (0.5, 0.75, 1.0),
        'vect__max_features': (None, 10000, 25000, 50000),
        'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
        'clf__C': np.arange(0.01, 1.01, 0.03),
        'clf__kernel': ["rbf", "linear"],
        'clf__class_weight': ["balanced"],
        "clf__decision_function_shape": ["ovo", "ovr"], }

    scorer = make_scorer(f1_score, average='macro')
    # cv=5 is a 5-fold cross validation
    gs_clf = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, cv=5, scoring=scorer)
    gs_clf.fit(train_features, y_train)
    print(gs_clf.best_params_)
    test_pred = gs_clf.predict(test_features)
    metrics += [f1_score(y_test, test_pred, average="macro"),
                precision_score(y_test, test_pred, average="macro"),
                recall_score(y_test, test_pred, average="macro"),
                accuracy_score(y_test, test_pred)
                ]
    if verbose:
        print('F1: {:.3f} | Pr: {:.3f} | Re: {:.3f} | Accuracy: {:.3f} \n'.format(*metrics))
    if confusion:
        print(confusion_matrix(y_test, test_pred))
    return gs_clf
