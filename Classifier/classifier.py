from sklearn import svm

def vectorize(indexes, sentence):
    b = [0]*len(indexes)
    for w in sentence.split():
        b[indexes[w]] += 1

    return b

with open('data.txt', 'r') as f:
	lines = [l.split(':') for l in f]

classes = {e[0] for e in lines}
words = {w for e in lines for w in e[1].split()}
#print classes
#print words

ind_Y = {key:ind for ind,key in enumerate(classes)}
ind_X = {key:ind for ind,key in enumerate(words)}
#print(ind_Y)
#print(ind_X)

Y = [ind_Y[l[0]] for l in lines]
#print(Y) 

X = [vectorize(ind_X, l[1]) for l in lines]
#print(X)

clf = svm.SVC()
clf.fit(X, Y)

print(clf.predict([vectorize(ind_X, "my head hurts")]))