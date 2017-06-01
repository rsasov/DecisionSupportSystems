from sklearn.feature_extraction import DictVectorizer
from sklearn.datasets import load_files

mappings = load_files('data', load_content=True, encoding='utf-8')
#print mappings
vec = DictVectorizer()
vec.fit_transform(mappings)
#print mappings.target_names



#sklearn.datasets.load_files('data', description=None, categories=None, 
#	load_content=True, shuffle=True, encoding='utf-8', decode_error='strict', random_state=0)

#sklearn.feature_extraction.DictVectorizer(dtype=<type 'numpy.float64'>, separator='=', sparse=True, sort=True)