from __future__ import division
from sklearn import svm
import random

def vectorize(indexes, sentence):
    b = [0]*len(indexes)
    for w in sentence.split():
        b[indexes[w]] += 1

    return b

with open('data.txt', 'r') as f:
	lines = [l.split(':') for l in f]

classes = {e[0] for e in lines}
words = {w for e in lines for w in e[1].rstrip().split()}

#print classes
#print words

ind_Y = {key:ind for ind,key in enumerate(classes)}
ind_X = {key:ind for ind,key in enumerate(words)}
#print(ind_Y)
#print(ind_X)

Y = [ind_Y[l[0]] for l in lines]
#print(Y) 

X = [vectorize(ind_X, l[1]) for l in lines]


shuffled = zip(X, Y)
random.shuffle(shuffled)
training = shuffled[len(shuffled)//10:]
test = shuffled[:len(shuffled)//10]
x_test, y_test = zip(*test)
x_training, y_training = zip(*training)
#print(X)

clf = svm.SVC()
clf.fit(x_training, y_training)

#accuracy = sum(clf.predict(x) == y for x,y in zip(x_test, y_test)) / len(y_test)
#print accuracy

accuracy = sum(clf.predict(x) == y for x,y in zip(x_training, y_training)) / len(y_training)
print accuracy