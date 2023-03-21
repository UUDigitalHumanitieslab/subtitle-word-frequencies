import os
import csv

from metadata.summary import summarise_genres

def test_summary(tmpdir):
    here = os.path.dirname(__file__)
    metadata_file = os.path.join(here, 'testdata/Word_frequency_qry.xlsx')
    summary_file = os.path.join(tmpdir, 'summary.csv')

    summarise_genres(metadata_file, summary_file)

    with open(summary_file) as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ['categorie', 'subcategorie', 'uitzendingen', 'zendtijd']
        rows = [row for row in reader]
        assert len(rows) == 2

        expected = [
            {
                'categorie': 'Informatief',
                'subcategorie': 'Nieuws/actualiteiten',
                'uitzendingen': '2',
                'zendtijd': '50'
            }, {
                'categorie': 'Informatief',
                'subcategorie': 'Spel/quiz',
                'uitzendingen': '1',
                'zendtijd': '30'
            }
        ]

        for row, exptected_row in zip(rows, expected):
            assert row == exptected_row