import utils
from collections import namedtuple


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


def quality_score(tp, tn, fp, fn):
    if tp*tn*fn == 0:
        return 0
    quality = (tp + tn) / (tp + tn + 10 * fp + fn)
    return quality


def compute_quality_for_corpus(corpus_dir):
    truth_file_path = corpus_dir + '\\1\\!truth.txt'
    prediction_file_path = corpus_dir + '\\2\\!prediction.txt'
    truth_dict = utils.read_classification_from_file(truth_file_path)
    pred_dict = utils.read_classification_from_file(prediction_file_path)
    confusion_matrix = compute_confusion_matrix(truth_dict, pred_dict)
    tp = getattr(confusion_matrix, 'tp')
    tn = getattr(confusion_matrix, 'tn')
    fp = getattr(confusion_matrix, 'fp')
    fn = getattr(confusion_matrix, 'fn')
    quality = quality_score(tp, tn, fp, fn)
    return quality


if __name__ == '__main__':
    q = compute_quality_for_corpus('corpus_for_testing_delete_me')
    print(q)
