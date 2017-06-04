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

proportion = int(len(words)*0.9)
train_words = set(random.sample(words, proportion))
test_words = words - train_words

#print classes
print train_words
print "\n\n"
print test_words

ind_Y = {key:ind for ind,key in enumerate(classes)}
#ind_X = {key:ind for ind,key in enumerate(words)}
ind_X_train = {key:ind for ind,key in enumerate(train_words)}
ind_X_test = {key:ind for ind,key in enumerate(test_words)}
#print(ind_Y)
#print(ind_X)

Y = [ind_Y[l[0]] for l in lines]
#print(Y) 

X = [vectorize(ind_X_train, l[1]) for l in lines]
X_test = [vectorize(ind_X_test, l[1]) for l in lines]
#print(X)

clf = svm.SVC()
clf.fit(X, Y)

print(clf.predict(X_test))