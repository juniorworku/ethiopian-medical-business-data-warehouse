# Task 2: Data Cleaning and Transformation

## Overview

This task involves cleaning and transforming the scraped data from Ethiopian medical businesses on Telegram channels. The process includes removing duplicates, handling missing values, standardizing formats, validating data, and storing cleaned data in a database. Additionally, we use DBT (Data Build Tool) to perform data transformations and ensure data quality.

## Steps

### 1. Data Cleaning

Data cleaning involves:
- Removing duplicates
- Handling missing values
- Standardizing formats
- Data validation

#### Script: `cleaning_transforing/clean_transform.py`

This script performs the data cleaning operations and saves the cleaned data to the `cleaning_transforming/data/cleaned_transformed` directory.

#### Usage

```bash
cd cleaning_transforming
python clean_transform.py
