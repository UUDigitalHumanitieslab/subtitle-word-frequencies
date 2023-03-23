from sklearn.feature_extraction.text import CountVectorizer

def make_vectoriser(text):
    cv = CountVectorizer()
    cv.fit(text)
    return cv
