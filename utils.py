from collections import namedtuple


def read_classification_from_file(fpath):
    cls_file = open(fpath, "r")
    cls_dict = dict()
    for line in cls_file.readlines():
        cls_dict.update({line.split(None)[0]: line.split(None)[1]})
    cls_file.close()
    return cls_dict


def write_classification_to_file(cls_dict, fpath):
    cls_file = open(fpath, "w+")
    for email, tag in cls_dict.items():
        cls_file.write(email + ' ' + tag + '\n')
    cls_file.close()


def compute_confusion_matrix(truth_dict, pred_dict, pos_tag='SPAM', neg_tag='OK'):
    ConfMat = namedtuple('ConfMat', 'tp tn fp fn')
    if len(truth_dict) == 0 and len(pred_dict) == 0:
        return ConfMat(tp=0, tn=0, fp=0, fn=0)
    else:
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for email, tag in truth_dict.items():
            if tag == pred_dict.get(email) and pos_tag == tag:
                tp = tp + 1
            if tag == pred_dict.get(email) and neg_tag == tag:
                tn = tn + 1
            if tag != pred_dict.get(email) and pos_tag == pred_dict.get(email):
                fp = fp + 1
            if tag != pred_dict.get(email) and neg_tag == pred_dict.get(email):
                fn = fn + 1
        return ConfMat(tp=tp, tn=tn, fp=fp, fn=fn)
