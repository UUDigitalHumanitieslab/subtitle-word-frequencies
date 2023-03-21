# Make a summary of the metadata

import os
import sys
import csv
from functools import reduce

from metadata.parse import parse

def summarise_genres(metadata_path, summary_path):
    '''Read the metadata file and write a csv summary'''

    data = parse(metadata_path)
    aggregated_genres = aggregate_genres(data)

    with open(summary_path, 'w') as f:
        writer = csv.DictWriter(f,
            fieldnames = ['categorie', 'uitzendingen', 'zendtijd'])
        writer.writeheader()
        for row in aggregated_genres:
            writer.writerow(row)

def aggregate_genres(rows):
    '''Aggregate genres from data'''

    data_by_genre = reduce(
        add_row_to_genre_aggregation,
        rows,
        dict()
    )
    return data_by_genre.values()

def add_row_to_genre_aggregation(data_by_genre, row):
    genre = row['category']
    duration = row['program_duration'] or 0

    if genre not in data_by_genre:
        data_by_genre[genre] = {
            'categorie': genre,
            'uitzendingen': 1,
            'zendtijd': duration
        }
    else:
        data_by_genre[genre]['uitzendingen'] += 1
        data_by_genre[genre]['zendtijd'] += duration

    return data_by_genre

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

def find_metadata_file():
    '''Find the metadata file in the excel directory'''
    xlsx_files = filter(lambda filename: filename.endswith('.xlsx'), os.listdir(data_dir))
    return os.path.join(data_dir, next(xlsx_files, ''))

if __name__ == '__main__':
    if len(sys.argv) > 2:
        metadata_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        metadata_file = find_metadata_file()
        output_file = os.path.join(data_dir, 'summary.csv')
        
    if not os.path.isfile(metadata_file):
        print('Metadatafile {} does not exist!'.format(metadata_file))
    else:
        summarise_genres(metadata_file, output_file)
        print('Done! Output file in {}'.format(os.path.abspath(output_file)))