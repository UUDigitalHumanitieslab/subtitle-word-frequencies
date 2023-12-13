import spacy
from frog import Frog, FrogOptions

class Lemmatizer():

    def __init__(self, method='spacy'):
        self.method = method
        if self.method == 'spacy':
            self._setup_spacy()
        if method == 'frog':
            self._setup_frog()

    def process(self, text):
        if self.method == 'spacy':
            return self._process_spacy(text)
        if self.method == 'frog':
            return self._process_frog(text)

    def _setup_spacy(self):
        self.nlp = spacy.load('nl_core_news_sm')
        lemmatizer = self.nlp.get_pipe('lemmatizer')

    def _process_spacy(self, text):
        doc = self.nlp(text)
        lemmas = (token.lemma_ for token in doc)
        return ' '.join(lemmas)

    def _setup_frog(self):
        self.frog = Frog(FrogOptions(parser=False))

    def _process_frog(self, text):
        output = self.frog.process(text)
        lemmas = (token['lemma'] for token in output)
        return ' '.join(lemmas)
