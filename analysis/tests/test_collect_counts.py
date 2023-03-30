import csv
import os
from analysis.collect_counts import collect_token_counts, save_counts

def test_collect_counts(metadata_filename, data_directory):
    genres, vocab, tdm = collect_token_counts(metadata_filename, data_directory)
    assert len(genres) == 2
    assert len(vocab) == 8
    assert tdm.shape == (2,8)

    assert genres == [('Informatief', 'Nieuws/actualiteiten'), ('Informatief', 'Spel/quiz')]
    term_index = lambda term: next(i for i, t in enumerate(vocab) if t == term)
    assert tdm[0, term_index('hallo')] == 3
    assert tdm[1, term_index('hallo')] == 0

def test_save_counts(metadata_filename, data_directory, tmpdir):
    csv_filename = os.path.join(tmpdir, 'counts.csv')
    genres, vocab, tdm = collect_token_counts(metadata_filename, data_directory)
    save_counts(csv_filename, genres, vocab, tdm)

    with open(csv_filename) as csv_file:
        reader = csv.DictReader(csv_file)
        assert 'Term' in reader.fieldnames
        assert 'Informatief - Nieuws/actualiteiten' in reader.fieldnames

        rows = [row for row in reader]
        assert len(rows) == len(vocab)
