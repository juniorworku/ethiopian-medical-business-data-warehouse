import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_USER = 'postgres'
DB_PASSWORD = 'new_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'

# List of CSV files and corresponding table names
csv_files = {
    'Chemed.csv': 'chemed',
    'DoctorsET.csv': 'doctorset',
    'EAHCI.csv': 'eahci',
    'lobelia4cosmetics.csv': 'lobelia4cosmetics',
    'yetenaweg.csv': 'yetenaweg'
}

# Create a database engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load each CSV file into the PostgreSQL database
for csv_file, table_name in csv_files.items():
    df = pd.read_csv(f'./data/cleaned_transformed/{csv_file}')
    df.to_sql(table_name, engine, schema='raw', if_exists='replace', index=False)
    print(f'{csv_file} loaded into PostgreSQL table raw.{table_name}')
