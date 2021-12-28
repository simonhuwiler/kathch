# Kath.ch Data Analysis
How does the catholic media portal kath.ch work on daily bases? A quantitative analysis.

## Installation
Windows
```console
pip venv env
env\Scripts\activate
pip install -r requirements.txt
```
Mac/Linux

```console
pip venv env
source env/bin/activate on mac
pip install -r requirements.txt
```
## Scrape data
Run `src/1_daily.py` as you wish (daily). It will push new articles into the git repo. You need to set up ssh keys on your server.

## Extract data
Run `src/2_extract_files.ipynb`. This will generate json-files from html-articles.

## Analyse
See `3_analyse.ipynb`

## Published articles based on this code
[Konservative Katholiken schiessen sich auf das knallige Medienportal der Kirche ein – und haben damit Erfolg](https://www.nzz.ch/schweiz/konservative-kritisieren-kathch-und-haben-damit-erfolg-ld.1661201)

## Contact
www.journalist.sh