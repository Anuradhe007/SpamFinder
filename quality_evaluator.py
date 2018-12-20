import simplefilters
import quality
import os

nf = simplefilters.RandomFilter()
nf.train('C:\\Users\\Prabhath\\Desktop\\spam_filter\\1' + '\\!truth.txt')
nf.test('C:\\Users\\Prabhath\\Desktop\\spam_filter\\2')
print(quality.compute_quality_for_corpus('C:\\Users\\Prabhath\\Desktop\\spam_filter'))
os.remove("C:\\Users\\Prabhath\\Desktop\\spam_filter\\2\\!prediction.txt")