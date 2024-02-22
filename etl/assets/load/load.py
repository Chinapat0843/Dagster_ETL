from dagster import  asset 
from etl.resources.db_conn import get_postgres_conn

import pandas as pd
from etl.assets.extract.extract_local_file import read__person , read__condition_occurrence , read__drug_exposure
from etl.assets.transform.transform import topten_condition_occurrence
import logging


# load local files to postgresSQL database
@asset( group_name="load", compute_kind="pandas", io_manager_key="db_io")
def source__person(context, read__person: pd.DataFrame) -> pd.DataFrame:
    """Transform and Stage Data into Postgres."""
    try:
        context.log.info(read__person.head())
        df = read__person
        return df
    except Exception as e:
        context.log.info(str(e))

@asset( group_name="load", compute_kind="pandas", io_manager_key="db_io")
def source__condition_occurrence(context, read__condition_occurrence: pd.DataFrame) -> pd.DataFrame:
    """Transform and Stage Data into Postgres."""
    try:
        context.log.info(read__condition_occurrence.head())
        df = read__condition_occurrence
        return df
    except Exception as e:
        context.log.info(str(e))

@asset( group_name="load", compute_kind="pandas", io_manager_key="db_io")
def source__drug_exposure(context, read__drug_exposure: pd.DataFrame) -> pd.DataFrame:
    """Transform and Stage Data into Postgres."""
    try:
        context.log.info(read__drug_exposure.head())
        df = read__drug_exposure
        return df
    except Exception as e:
        context.log.info(str(e))


# Load tranformation data to postgresSQL database
@asset(group_name="Transform_load", compute_kind="pandas", io_manager_key="db_io")
def T_topten_condition_occurrence(context, topten_condition_occurrence: pd.DataFrame) -> pd.DataFrame:
    """Transform and Stage Data into Postgres."""
    try:
        context.log.info(topten_condition_occurrence.head())
        df = topten_condition_occurrence
        return df
    except Exception as e:
        context.log.info(str(e))