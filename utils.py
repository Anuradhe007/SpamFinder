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


if __name__ == "__main__":
    cls_dict = read_classification_from_file('/home/anuradha/Desktop/spam_filter/spam-data-12-s75-h25/1/!truth.txt')
    write_classification_to_file(cls_dict, '/home/anuradha/Desktop/spam_filter/spam-data-12-s75-h25/1/!test.txt')
