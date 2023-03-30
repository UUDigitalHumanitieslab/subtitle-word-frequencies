from analysis.count import *

texts = [
    'Willem die Madocke maecte,',
    'Daer hi dicken omme waecte,',
    'Hem vernoyde so haerde',
    'Dat die avonture van Reynaerde',
    'In Dietsche onghemaket bleven',
    'Die Arnout niet hevet vulscreven',
    'Dat hi die vijte dede soucken',
    'Ende hise na den Walschen boucken',
    'In Dietsche dus hevet begonnen',
]

def test_vocab():
    cv, _ = make_vectoriser(texts)
    vocab = list(cv.get_feature_names_out())
    
    assert 'hi' in vocab
    assert all(
        word == word.lower() for word in vocab
    )

def test_counts():
    cv, tdm = make_vectoriser(texts)
    vocab_size = cv.get_feature_names_out().size
    assert tdm.shape == (len(texts), vocab_size)

    totals = total_frequencies(tdm)
    assert totals.shape == (1, vocab_size)