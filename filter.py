import os
import math
import re
from collections import Counter
import utils


class MyFilter:

    def __init__(self):
        self.spams = Counter()
        self.hams = Counter()
        self.spamicity = {}
        self.regexp = re.compile(r"(?:(?:\w+(?:\.\w+)*@)?(?:[a-zA-Z0-9_]+\.)+[a-z]{2,12})|[a-zA-Z0-9]+")

    def get_tokens(self, s):  # get list of tokens for given string
        return [word.lower() for word in self.regexp.findall(s) if len(word) < 30]

    def test(self, dir):
        EASING = 0.095
        SLICING = 38
        cls_dict = dict()
        file_name_with_data = dict()

        for filename in os.listdir(dir):
            if filename[0] == "!": continue
            f = open(dir + '/' + filename, 'r', encoding="utf8")
            file_name_with_data.update({filename: f.read()})

        for file_name, email_content in file_name_with_data.items():
            a, b = 1.0, 1.0

            for word, spamicity in \
                    sorted( \
                            [(w, 0.5 if self.spamicity.get(w) == None else self.spamicity[w]) \
                             for w in self.get_tokens(email_content)], \
                            key=lambda x: 0.5 - math.fabs(0.5 - x[1]) \
                            )[0:SLICING]:
                a *= math.fabs(spamicity - EASING)
                b *= 1.0 - spamicity + EASING
                cls_dict.update({file_name: ("SPAM" if (a / (a + b)) >= 1.0 else "OK")})
        utils.write_classification_to_file(cls_dict, dir + "/!prediction.txt")

    def train(self, dir):
        classification = utils.read_classification_from_file(dir + "/!truth.txt")
        spam_total = 0
        ham_total = 0
        file_name_with_data = dict()

        for filename in os.listdir(dir):
            if filename[0] == "!": continue
            f = open(dir + "/" + filename, 'r', encoding="utf8")
            file_name_with_data.update({filename: f.read()})

        for file_name, email_content in file_name_with_data.items():
            cls = classification[file_name]

            if cls == "SPAM":
                spam_total += 1
            else:
                ham_total += 1

            for word in set(self.get_tokens(email_content)):
                if cls == "SPAM":
                    self.spams[word] += 1
                else:
                    self.hams[word] += 1

        spam_probability = spam_total / (spam_total + ham_total)
        ham_probability = 1 - spam_probability

        for word in (set(self.spams.keys()) | set(self.hams.keys())):
            self.spamicity[word] = (self.spams[word] / spam_total * spam_probability) / \
                                   (self.spams[word] / spam_total * spam_probability + self.hams[
                                       word] / ham_total * ham_probability)
