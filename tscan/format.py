import csv
import pandas


def convert_to_tscan_format(input_file, output_file):
    df = pandas.read_csv(input_file)
    prepare_data(df)


def get_total_frequencies(df: pandas.DataFrame):
    genres = df.columns[1:]

    terms = df['Term']
    freq = df.loc[:, genres].sum(axis=1)

    result = pandas.DataFrame({
        'term': terms,
        'freq': freq,
    })

    return result.sort_values(by='freq', ascending=False)


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


def prepare_data(df: pandas.DataFrame):
    freqs = get_total_frequencies(df)
    complete = add_relative_and_cumulative(freqs)

    print(complete)
