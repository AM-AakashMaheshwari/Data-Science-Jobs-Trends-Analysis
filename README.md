# Data Scientist Job Trend ETL Project

This project analyzes Data Scientist job listings scraped from Glassdoor. The goal is to help a consulting firm understand hiring trends, salary ranges, and skill demand across industries.

## Features
- Cleans messy and inconsistent job data
- Parses and extracts salary ranges
- Flags job seniority and remote positions
- Structures a modular ETL pipeline using Python (Pandas)

## ETL Flow
1. `extract.py`: Reads raw CSV
2. `transform.py`: Cleans and transforms the data
3. `load.py`: Saves cleaned data
4. `run_pipeline.py`: Orchestrates the pipeline

## Technologies
- Python
- Pandas
- CSV

## Usage
```bash
python run_pipeline.py
