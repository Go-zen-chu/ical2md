# ical2md

## About
Simple script for converting ical to markdown.

## Install
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Run
```
python main.py -i ~/Desktop/your.ics -e ~/Desktop/md_dir -f "2016-01-01" -t "2017-12-31"
```

## Help
```
usage: main.py [-h] -i ICAL -e EXPORT [-f FROM_DATE] [-t TO_DATE]

Convert ical to markdown

optional arguments:
  -h, --help            show this help message and exit
  -i ICAL, --ical ICAL  ical file path for input
  -e EXPORT, --export EXPORT
                        md export dir path
  -f FROM_DATE, --from-date FROM_DATE
                        From date
  -t TO_DATE, --to-date TO_DATE
                        To date
```
