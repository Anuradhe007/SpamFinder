def quality_score(tp, tn, fp, fn):
    q = tp + tn/(tp+tn+10*fp+fn)

    if 0 <= q < 0.3:
        return 0
    elif 0.3 <= q < 0.5:
        return 1
    elif 0.5 <= q < 0.7:
        return 2
    elif 0.7 <= q < 0.9:
        return 2.5
    elif 0.9 <= q < 1:
        return 3
