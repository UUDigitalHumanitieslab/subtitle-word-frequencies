from analysis.collect_counts import collect_token_counts

def test_collect_counts(metadata_filename, data_directory):
    genres, vocab, tdm = collect_token_counts(metadata_filename, data_directory)
    assert len(genres) == 2
    assert len(vocab) == 8
    assert tdm.shape == (2,8)

    assert genres == [('Informatief', 'Nieuws/actualiteiten'), ('Informatief', 'Spel/quiz')]
    term_index = lambda term: next(i for i, t in enumerate(vocab) if t == term)
    assert tdm[0, term_index('hallo')] == 3
    assert tdm[1, term_index('hallo')] == 0