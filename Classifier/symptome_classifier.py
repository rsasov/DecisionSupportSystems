from sklearn import svm
import pickle

#vectorize expression
def vectorize(indexes, sentence):
    b = [0]*len(indexes)
    for w in sentence.split():
        b[indexes[w]] += 1

    return b

def save_obj(obj, name):
    with open('obj-'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

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

# Y parameter for classifier : classes
Y = [ind_Y[l[0]] for l in lines]
# X parameter for classifier (with vectorization) : expressions
X = [vectorize(ind_X, l[1]) for l in lines]

#linear support vector machine
lin_clf = svm.LinearSVC()
lin_clf.fit(X, Y)

save_obj(inv_ind_Y, 'reverse_classes_mapping')
save_obj(ind_X, 'words_mapping')
save_obj(lin_clf, 'linear_classifier')