from analysis.lemmatize import Lemmatizer

text = 'Een woord is het kleinste zelfstandig gebruikte taalelement, ' \
    'dat in de spreektaal is opgebouwd uit klanken en in de geschreven ' \
    'taal uit letters.'

expected = 'een woord zijn het klein zelfstandig gebruiken taalelement , ' \
    'dat in de spreektaal zijn opbouwen uit klanken en in de schrijven ' \
    'taal uit letter .'


def test_lemmatize():
    lemmatizer = Lemmatizer()
    result = lemmatizer.process(text)
    assert result == expected
