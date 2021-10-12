from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix


# function that returns performance metrics and confusion matrix / only prints to console
def get_performance(labels, pred, classNames, score="macro"):
    f1 = f1_score(labels, pred, average=score)
    prec = precision_score(labels, pred, average=score)
    rec = recall_score(labels, pred, average=score)
    acc = accuracy_score(labels, pred)
    print("Prec: ", prec, "; Rec: ", rec, "F1: ", f1, "; Acc: ", acc)
    print(confusion_matrix(labels, pred))
    mat = confusion_matrix(labels, pred, labels=classNames)
    return mat
