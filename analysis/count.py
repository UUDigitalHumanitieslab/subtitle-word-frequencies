from sklearn.feature_extraction.text import CountVectorizer

def make_vectoriser(texts):
    cv = CountVectorizer()
    cv.fit(texts)
    return cv

def count_tokens(cv: CountVectorizer, texts):
    '''Return a sparse matrix of term frequencies per text'''
    return cv.transform(texts)

def total_frequencies(tdm):
    '''Get total frequencies from a term-document matrix'''
    return tdm.sum(0)
