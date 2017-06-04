#!/usr/bin/env python2

from sys import argv
from sklearn import svm
import pickle

#vectorize expression
def vectorize(indexes, sentence):
    b = [0]*len(indexes)
    for w in sentence.split():
        b[indexes[w]] += 1

    return b

def load_obj(name):
    with open('obj-' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def predict(sentence):
	ind_X = load_obj('words_mapping')
	rev_ind_Y = load_obj('reverse_classes_mapping')
	lin_clf = load_obj('linear_classifier')

	X = [vectorize(ind_X, s[1]) for s in sentence.rstrip().split()]
	return rev_ind_Y[lin_clf.predict(X)[0]]

if __name__ == "__main__":
	print(predict(argv[1]))