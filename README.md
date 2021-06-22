# Kath.ch Data Analysis
How does the catholic media portal kath.ch work on daily bases? A quantitative analysis.

## Installation
```
pip venv env
env\Scripts\activate #or source env/bin/activate on mac
pip install requirements.txt
```
## Scrape data
Run `src/1_daily.py` as you wish (daily). It will push new articles into the git repo. You need to set up ssh keys on your server.

## Extract data
Run `src/2_extract_files.ipynb`. This will generate json-files from html-articles.

## Analyse
See `3_analyse.ipynb`

## Contact
www.journalist.sh