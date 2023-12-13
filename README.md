# subtitle-word-frequencies

Code for analysing subtitle data from the NPO and extracting word frequency tables.

## Requirements

Using a python environment, install requirements with `pip install -r requirements.txt`. 

### Lemmatisers

To perform lemmatisation, you'll also need to download data for spacy and/or frog.

After installing the requirements, run:

```sh
python -m spacy download nl_core_news_sm
python -c "import frog; frog.installdata()"
```

To add new python packages, add them to `requirements.in` and run `pip-compile requirements.in --outputfile requirements.txt`.

## Unit tests

Run unit tests with `pytest`

## Usage

The following commands are supported.

### Summary of genres

You can create a csv file that lists the genres and the number of files + total runtime per genre specified in the metadata spreadsheet. To run this:

```bash
python -m metadata.summary
```

to create a summary of the metadata file located in `/data`, assuming your data folder contains a single xlsx file.

You can also specify the location:

```bash
python -m metadata.summary path/to/metadata.xlsx path/to/output.csv
```

### Save token frequencies

You can count token frequencies in the data and export them to a csv with:

```bash
python -m analysis.collect_counts
```

You can also specify the input data, the output location, and add a lemmatiser. By default, no lemmatisation will be applied. Options for the lemmatiser are `frog` and `spacy`.

```bash
python -m analysis.collect_counts path/to/metadata.xlsx --output path/to-output.csv --lemmatizer frog
```

The resulting csv file lists the frequency for each word, split by genre. If you specified a lemmatiser, frequencies are given by lemma instead.
