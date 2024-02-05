import csv
import pandas

MIN_COUNT = 2

def convert_to_tscan_format(input_file, output_file):
    '''
    Convert a CSV file with frequencies to t-scan's format.

    This file does not include headers and is tab-separated.
    Each row respectively lists:
    - the term
    - the absolute frequency
    - the cumulative absolute frequency
    - the cumulative percentile frequency
    Rows are sorted in descending order of frequency
    '''
    
    df = pandas.read_csv(input_file)
    processed = prepare_data(df)
    save_data(processed, output_file)


def get_filtered_frequencies(df: pandas.DataFrame):
    terms = df['Term']
    freq = df['Count']

    result = pandas.DataFrame({
        'term': terms,
        'freq': freq,
    })

    filtered = result[result['freq'] >= MIN_COUNT]

    return filtered.sort_values(by='freq', ascending=False)


def add_relative_and_cumulative(df: pandas.DataFrame):
    total = df['freq'].sum()

    freq_rel = 100 * df['freq'] / total
    freq_abs_cum = df['freq'].cumsum()
    freq_rel_cum = freq_rel.cumsum()

    return pandas.DataFrame({
        'term': df['term'],
        'freq_abs': df['freq'],
        'freq_rel': freq_rel,
        'freq_abs_cum': freq_abs_cum,
        'freq_rel_cum': freq_rel_cum,
    })


def save_data(df: pandas.DataFrame, output_path: str):
    with open(output_path, 'w') as output_io:
        for _, row in df.iterrows():
            content = '{}\t{}\t{}\t{}\n'.format(
                row['term'],
                row['freq_abs'],
                row['freq_abs_cum'],
                row['freq_rel_cum'],
            )
            output_io.write(content)

def prepare_data(df: pandas.DataFrame):
    freqs = get_filtered_frequencies(df)
    complete = add_relative_and_cumulative(freqs)
    return complete
