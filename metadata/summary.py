# Make a summary of the metadata

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
    duration = row['program_duration']

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