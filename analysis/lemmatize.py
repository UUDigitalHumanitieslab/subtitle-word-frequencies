import spacy


class Lemmatizer():

    def __init__(self):
        self.nlp = spacy.load('nl_core_news_sm')
        lemmatizer = self.nlp.get_pipe('lemmatizer')

    def process(self, text):
        doc = self.nlp(text)
        lemmas = (token.lemma_ for token in doc)
        return ' '.join(lemmas)
