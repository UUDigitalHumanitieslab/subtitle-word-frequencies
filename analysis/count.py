from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def make_vectoriser(texts):
    cv = CountVectorizer()
    tdm = cv.fit_transform(texts)
    return cv, tdm

def total_frequencies(tdm):
    '''Get total frequencies from a term-document matrix'''
    summed = tdm.sum(0)
    flat = np.asarray(summed).squeeze().tolist()
    return flat
