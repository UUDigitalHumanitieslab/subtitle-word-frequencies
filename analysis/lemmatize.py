import spacy
from frog import Frog, FrogOptions
import click
from tqdm import tqdm

from vtt.convert_to_plain import list_plain_text_files, replace_suffix, PLAIN_EXTENSION

LEMMAS_EXTENSION = '.lemmas.txt'

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

def export_lemmatized(plain_text_filename, lemmatizer):
    with open(plain_text_filename) as infile:
        lines = infile.readlines()

    output_filename = replace_suffix(plain_text_filename, PLAIN_EXTENSION, LEMMAS_EXTENSION)

    with open(output_filename, 'w') as outfile:
        for line in lines:
            lemmas = lemmatizer.process(line)
            outfile.write(lemmas)

    return output_filename

@click.command()
@click.argument(
    'directory',
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
)
@click.option(
    '--frog', 'method', flag_value='frog', default=True,
    help='lemmatise using Frog (default)',
)
@click.option(
    '--spacy', 'method', flag_value='spacy',
    help='lemmatise using spaCy',
)
def run(directory, method):
    '''
    Exports lemmatised versions of plain text files in DIRECTORY exported by the
    vtt.convert_to_plain script.
    '''

    lemmatizer = Lemmatizer(method)
    files = list_plain_text_files(directory)
    
    for file in tqdm(files):
        export_lemmatized(file, lemmatizer)
    
    print('Done!')

if __name__ == '__main__':
    run()