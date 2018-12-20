import utils
import os
import random


class NaiveFilter:
    def train(self, path_to_training_corpus):
        self.trained_data_dict = utils.read_classification_from_file(path_to_training_corpus)

    def test(self, path_to_corpus_to_evaluate):
        files = os.listdir(path_to_corpus_to_evaluate)
        cls_dict = dict()
        for name in files:
            cls_dict.update({name: 'OK'})
        utils.write_classification_to_file(cls_dict, path_to_corpus_to_evaluate)


class ParanoidFilter:
    def train(self, path_to_training_corpus):
        self.trained_data_dict = utils.read_classification_from_file(path_to_training_corpus)

    def test(self, path_to_corpus_to_evaluate):
        files = os.listdir(path_to_corpus_to_evaluate)
        cls_dict = dict()
        for name in files:
            cls_dict.update({name: 'SPAM'})
        utils.write_classification_to_file(cls_dict, path_to_corpus_to_evaluate)


class RandomFilter:
    def train(self, path_to_training_corpus):
        self.trained_data_dict = utils.read_classification_from_file(path_to_training_corpus)

    def test(self, path_to_corpus_to_evaluate):
        files = os.listdir(path_to_corpus_to_evaluate)
        cls_dict = dict()
        type_list = ['SPAM', 'OK']

        for name in files:
            cls_dict.update({name: type_list[random.randint(0, 1)]})
        utils.write_classification_to_file(cls_dict, path_to_corpus_to_evaluate)
