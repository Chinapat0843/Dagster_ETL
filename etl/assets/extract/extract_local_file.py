from dagster import  asset 
from etl.resources.db_conn import get_postgres_conn
import pandas as pd
import logging

#read csv file from local path
@asset(group_name="Extract", compute_kind="pandas" , io_manager_key="file_io")
def read__person(context )  -> pd.DataFrame:
    #file_path = r'{}'.format(path_file)
    file_path = r'./data/person.csv'
    df = pd.read_csv(file_path)
    context.log.info(f'Read {len(df)} rows from {file_path}')
    return df

@asset(group_name="Extract", compute_kind="pandas" , io_manager_key="file_io")
def read__condition_occurrence(context )  -> pd.DataFrame:
    #file_path = r'{}'.format(path_file)
    file_path = r'./data/condition_occurrence.csv'
    df = pd.read_csv(file_path)
    context.log.info(f'Read {len(df)} rows from {file_path}')
    return df

@asset(group_name="Extract", compute_kind="pandas" , io_manager_key="file_io")
def read__drug_exposure(context )  -> pd.DataFrame:
    #file_path = r'{}'.format(path_file)
    file_path = r'./data/drug_exposure.csv'
    df = pd.read_csv(file_path)
    context.log.info(f'Read {len(df)} rows from {file_path}')
    return df

