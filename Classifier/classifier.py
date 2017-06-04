from __future__ import division
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = (15, 15)
plt.rcParams['image.interpolation'] = 'nearest'
from sklearn import svm
import random
import numpy as np

#vectorize expression
def vectorize(indexes, sentence):
    b = [0]*len(indexes)
    for w in sentence.split():
        b[indexes[w]] += 1

    return b

#display confusion matrix with colored gradient
def show_matrix(matrix, title='No title', c_label=""):
    plt.figure()
    plt.imshow(matrix, cmap='YlGnBu', interpolation='nearest')
    c = plt.colorbar()
    c.set_label(c_label)
    l = matrix.shape[0]
    plt.xticks(range(l))
    plt.xlabel("Ground truth")
    _ = plt.yticks(range(l))
    plt.ylabel("Predictions")
    plt.title(title)

#open data file and read it
with open('data.txt', 'r') as f:
	lines = [l.split(':') for l in f]

#store classes
classes = {e[0] for e in lines}
#store words by splitting expressions
words = {w for e in lines for w in e[1].rstrip().split()}

#mapping strings with int ident
ind_Y = {key:ind for ind,key in enumerate(classes)}
inv_ind_Y = {key:ind for key,ind in enumerate(classes)}
ind_X = {key:ind for ind,key in enumerate(words)}

#for testing purpose only
#show classes repartition
print(len(words))
count_classes = []
for c in lines:
        count_classes.append(ind_Y[c[0]])
for i in classes:
    print("%s: %d" % (i, count_classes.count(ind_Y[i])))

_ = plt.hist(count_classes, 21)

# Y parameter for classifier : classes
Y = [ind_Y[l[0]] for l in lines]
# X parameter for classifier (with vectorization) : expressions
X = [vectorize(ind_X, l[1]) for l in lines]

#divide between training set and test set
shuffled = zip(X, Y)
random.shuffle(shuffled)
training = shuffled[len(shuffled)//10:]
test = shuffled[:len(shuffled)//10]
x_test, y_test = zip(*test)
x_training, y_training = zip(*training)

#linear support vector machine
lin_clf = svm.LinearSVC()
lin_clf.fit(x_training, y_training)

#testing on training set, fill confusion matrix 
mat_lin = np.zeros((len(inv_ind_Y),len(inv_ind_Y)))
for x,y in zip(x_training, y_training):
    truth = inv_ind_Y[y]
    prediction = inv_ind_Y[lin_clf.predict(x)[0]]
    print('{0} = {1}'.format(prediction, truth)) 
    mat_lin[ind_Y[truth],ind_Y[prediction]] += 1

#matrix display
show_matrix(mat_lin)

#accuracy computation
accuracy = sum(lin_clf.predict(x) == y for x,y in zip(x_test, y_test)) / len(y_test)
print accuracy

#testing on test data, fill confusion matrix
mat_lin = np.zeros((len(inv_ind_Y),len(inv_ind_Y)))
for x,y in zip(x_test, y_test):
    truth = inv_ind_Y[y]
    prediction = inv_ind_Y[lin_clf.predict(x)[0]]
    print('{0} = {1}'.format(prediction, truth)) 
    mat_lin[ind_Y[truth],ind_Y[prediction]] += 1

#matrix display
show_matrix(mat_lin)

#accuracy computation 
accuracy = sum(lin_clf.predict(x) == y for x,y in zip(x_test, y_test)) / len(y_test)
print accuracy