# Subtitle word frequencies

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10607189.svg)](https://doi.org/10.5281/zenodo.10607189)

This repository contains python scripts to extract word frequency data from a collection of subtitle files.

Notable features:
- Frequency lists can be output in the format used by [T-scan](https://github.com/UUDigitalHumanitieslab/tscan).
- Subtitle files can be split by the genres defined in an accompanying metadata file
- Text can be lemmatised using [Frog](https://frognlp.readthedocs.io/en/latest/) or [SpaCy](https://spacy.io/).

The purpose of this repository is to provide transparency in our data collection and to make it easier to repeat the frequency analysis on newer data in the future. It is not developed to be of general use, but we include a licence for reuse (see below).

## Contents

### Data

The scripts are designed for a collection of subtitles from the NPO (Dutch public broadcast). This dataset is _not_ provided in this repository and is not publicly available due to copyright restrictions. The Research Software Lab works on this data in agreement with the NPO, but we cannot share the data with others.

Our data encodes subtitles as [WebVTT files](https://en.wikipedia.org/wiki/WebVTT), with an accompanying metadata file included as an [.xlsx file](https://en.wikipedia.org/wiki/Office_Open_XML).

### Scripts

Scripts are written in [Python](https://www.python.org/) and are structured into the following modules:

- [analysis](/analysis/) for counting and lemmatising extracted text
- [metadata](/metadata/) for parsing the metadata file to extract filenames and genres
- [tscan](/tscan/) for creating output in the format used by T-scan
- [vtt](/vtt/) for extracting strings from .vtt files

## Requirements

You'll need:

- [Python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

Install required python packages with 

```bash
pip install -r requirements.txt
```

### Lemmatisers

To perform lemmatisation, you'll also need to download data for spacy and/or frog.

After installing the requirements, run:

```sh
python -m spacy download nl_core_news_sm
python -c "import frog; frog.installdata()"
```

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

## Developing

### Unit tests

Run unit tests with

 ```bash
pytest
```

To add new python packages, add them to `requirements.in` and run 

```bash
pip-compile requirements.in --outputfile requirements.txt
```


## Licence

This repository is shared under a [BSD 3-Clause licence](/LICENSE).
