from sklearn.feature_extraction.text import CountVectorizer

def make_vectoriser(texts):
    cv = CountVectorizer()
    tdm = cv.fit_transform(texts)
    return cv, tdm

def total_frequencies(tdm):
    '''Get total frequencies from a term-document matrix'''
    return tdm.sum(0)
