# ELT with DuckDB

This project demonstrates how to read data from multiple sources (CSV, Excel, and JSON) and utilize DuckDB as read and ingestion to database

## Table of Contents

- [Installation](#installation)
- [Preparation](#preparation)
- [Usage](#usage)

## Installation

To get started, make sure you have Python and pip installed. Then, install the required packages:

```bash
conda create --name duckdb_dev
````
```bash
conda activate duckdb_dev
```
```bash
pip install pandas openpyxl duckdb
````
Address the installation of postgreSQL with this link https://www.postgresql.org/download/

## Preparation 

Data analyst will work into Database which use PostgreSQL. Create the database with script on the path 
   - **Path**: `script/sql/create_table.sql`
   - **Description**: Create relational database on postgreSQL

## Usage

For running the solution, please prompt the main script, it will running python script on the repo with squence 
  	- **File to DuckDB** : import all files with different type to duckdb
    - **Duckdb to PostgreSQL** : ingest data from duckdb to postgre via duckdb PostgreSQL extension
Prompt with below code 
```bash
python main.py
```
