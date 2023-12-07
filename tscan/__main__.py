import click
import os

from .format import convert_to_tscan_format

here = os.path.dirname(__file__)
data_dir = os.path.join(here, '..', 'data')

default_input = os.path.join(data_dir, 'token_frequencies.csv')
default_output = os.path.join(data_dir, 'npo_2022_all_words.freq')


@click.command()
@click.option(
    '--input',
    default=default_input,
    help='CSV file to convert to tscan format',
    type=click.Path(exists=True),
    prompt='input file'
)
@click.option(
    '--output',
    default=default_output,
    help='Path of output CSV file',
    prompt='output file',
)
def format(input, output):
    convert_to_tscan_format(input, output)


if __name__ == '__main__':
    format()
