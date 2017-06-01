#from sklearn import svm

#X = [[0,0],[1,1]]
#y = [0,1]
#clf = svm.SVC()
#clf.fit(X,y)
#SVC(C=1.0, cache_size=200, class_weight=None, degree=3, gamma='auto', kernel='rbf', max_iter=-1, probability=False, random_state=Node, shrinking=True, tol=0.001, verbose=False)

#SYMPTOMS
id_sym = 0
sym_dict = dict()
#read file with symptom list
f = open('Symptoms_list', 'r')
for line in f:
	#store each symptom in a map<string,id>
	sym_dict[line.rstrip()] = id_sym
	id_sym += 1
f.close()
#print sym_dict ok working

#FORMULATIONS
id_word = 0
word_dict = dict()
form_list = list()
#read each symptom file 
sym_list = sym_dict.keys()
for sym in sym_list:
	f = open('%s' % sym, 'r')
	for line in f:
		#associate formules with corresponding symptom

		#for each symptom build a map<word,id> starting id at 0
		tmp_list = line.rstrip().split()
		for word in tmp_list:
			if not word in word_dict
				word_dict[word] = id_word
				id_word += 1
	f.close()
#print form_dict ok working
print id_word
print len(word_dict)

#total number of different words = vector_size = dict_size
#create vectors for each formules (vector indices = word id) 1 = is present, 0 = is not


#build X and y
#use SVM (Support Vector Machine)









#mappings = load_files('data', load_content=True, encoding='utf-8')
#print mappings
#vec = DictVectorizer()
#vec.fit_transform(mappings)
#print mappings.target_names

#sklearn.datasets.load_files('data', description=None, categories=None, 
#	load_content=True, shuffle=True, encoding='utf-8', decode_error='strict', random_state=0)

#sklearn.feature_extraction.DictVectorizer(dtype=<type 'numpy.float64'>, separator='=', sparse=True, sort=True)