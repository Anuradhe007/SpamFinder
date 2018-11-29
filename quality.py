import utils


def quality_score(tp, tn, fp, fn):
    quality = (tp + tn) / (tp + tn + 10 * fp + fn)
    return quality


def compute_quality_for_corpus(corpus_dir):
    truth_dict = utils.read_classification_from_file(corpus_dir + '!truth.txt')
    pred_dict = utils.read_classification_from_file(corpus_dir + '!prediction.txt')
    confusion_matrix = utils.compute_confusion_matrix(truth_dict, pred_dict)
    tp = getattr(confusion_matrix, 'tp')
    tn = getattr(confusion_matrix, 'tn')
    fp = getattr(confusion_matrix, 'fp')
    fn = getattr(confusion_matrix, 'fn')
    quality = quality_score(tp, tn, fp, fn)
    return quality
