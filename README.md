# unflaired

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A Python3 script that checks for post aged 1 hours+ that is not flaired, and generate a mod report.

## Requirement

* Python3.7+ (technically will work with python3.6)

* virtualenv

* valid Reddit API keys, mod status is optional

## Installation

* git pull

* create new virtualenv

* `pip3 install -r requirements.txt`

* copy `config.sample.toml` to `config.toml` and fill it with necessary values.

## Database

In order to prevent duplicate entries, a sqlite3 database is made. Create one by running `python3 create_database_file.py` inside the virtualenv terminal.