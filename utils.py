from collections import namedtuple


def read_classification_from_file(fpath):
    classification_file = open(fpath, "r")
    fileLines = classification_file.readlines()
    classification_dict = dict()
    for line in fileLines:
        tmp = {line.split(None)[0]: line.split(None)[1]}
        classification_dict.update(tmp)
    classification_file.close()
    return classification_dict


def write_classification_to_file(cls_dict, fpath):
    file = open(fpath, "w+")
    for name, val in cls_dict.items():
        file.write(name + ' ' + val + '\n')
    file.close()


def compute_confusion_matrix(truth_dict, pred_dict, pos_tag='SPAM', neg_tag='OK'):
    ConfMat = namedtuple('ConfMat', 'tp tn fp fn')
    if len(truth_dict) == 0 and len(pred_dict) == 0:
        return ConfMat(tp=0, tn=0, fp=0, fn=0)
    else:
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for email, stat in truth_dict.items():
            if stat == pred_dict.get(email) and pos_tag == stat:
                tp = tp + 1
            if stat == pred_dict.get(email) and neg_tag == stat:
                tn = tn + 1
            if stat != pred_dict.get(email) and pos_tag == pred_dict.get(email):
                fp = fp + 1
            if stat != pred_dict.get(email) and neg_tag == pred_dict.get(email):
                fn = fn + 1
        return ConfMat(tp=tp, tn=tn, fp=fp, fn=fn)
