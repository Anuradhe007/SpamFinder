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


if __name__ == '__main__':
    cls_dict = read_classification_from_file('corpus_for_testing_delete_me/!truth.txt')
    write_classification_to_file(cls_dict, 'corpus_for_testing_delete_me/!prediction.txt')
