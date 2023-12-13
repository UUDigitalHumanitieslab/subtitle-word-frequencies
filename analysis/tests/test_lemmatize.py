from analysis.lemmatize import Lemmatizer
from analysis.collect_counts import collect_token_counts

text = 'Een woord is het kleinste zelfstandig gebruikte taalelement, ' \
    'dat in de spreektaal is opgebouwd uit klanken en in de geschreven ' \
    'taal uit letters.'

expected_spacy = 'een woord zijn het klein zelfstandig gebruiken taalelement , ' \
    'dat in de spreektaal zijn opbouwen uit klanken en in de schrijven ' \
    'taal uit letter .'


def test_lemmatize_with_spacy():
    lemmatizer = Lemmatizer(method='spacy')
    result = lemmatizer.process(text)
    assert result == expected_spacy


expected_frog = 'een woord zijn het klein zelfstandig gebruiken taalelement , ' \
    'dat in de spreektaal zijn opbouwen uit klank en in de schrijven ' \
    'taal uit letter .'


def test_lemmatize_with_frog():
    lemmatizer = Lemmatizer(method='frog')
    result = lemmatizer.process(text)
    assert result == expected_frog


def test_lemmatiser_in_collection(metadata_filename, data_directory):
    _, vocab, _ = collect_token_counts(
        metadata_filename, data_directory
    )

    assert 'is' in vocab

    _, vocab, _ = collect_token_counts(
        metadata_filename, data_directory, lemmatizer='frog'
    )

    assert 'zijn' in vocab
    assert 'is' not in vocab

    _, vocab, _ = collect_token_counts(
        metadata_filename, data_directory, lemmatizer='spacy')

    assert 'zijn' in vocab
    assert 'is' not in vocab
