import click
import os

here = os.path.dirname(__file__)
data_dir = os.path.join(here, '..', 'data')

default_input = os.path.join(data_dir, 'token_frequencies.csv')
default_output = os.path.join(data_dir, 'token_frequencies_tscan.csv')


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
    print(input)
    print(output)


if __name__ == '__main__':
    format()
