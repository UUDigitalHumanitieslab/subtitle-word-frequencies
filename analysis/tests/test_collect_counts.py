import csv
import os
from analysis.collect_counts import collect_token_counts, save_counts

def test_collect_counts(data_directory):
    counts = collect_token_counts(data_directory, 'word')
    assert len(counts) == 8    
    assert ('hallo', 3) in counts

def test_save_counts(data_directory, tmpdir):
    csv_filename = os.path.join(tmpdir, 'counts.csv')
    counts = collect_token_counts(data_directory)
    save_counts(csv_filename, counts)

    with open(csv_filename) as csv_file:
        reader = csv.DictReader(csv_file)
        assert 'Term' in reader.fieldnames
        assert 'Count' in reader.fieldnames

        rows = [row for row in reader]
        assert len(rows) == len(counts)
