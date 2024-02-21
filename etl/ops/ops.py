from dagster import job, op, repository , Out , In
from etl.resources.db_conn import get_postgres_conn
import pandas as pd
import logging


@op(name="read_csv_file" , out=Out(io_manager_key="file_io"))
def read_csv_file(context) -> pd.DataFrame:
    file_path = r"./etl/sfo_q2_weather_sample.csv"
    df = pd.read_csv(file_path)
    context.log.info(f"Read {len(df)} rows from {file_path}")
    return df


@op(name="load_data", out=Out(io_manager_key="db_io"))
def load_data(context, read_csv_output: pd.DataFrame) -> pd.DataFrame:
    """Transform and Stage Data into Postgres."""
    try:
        context.log.info(read_csv_output.head())
        df = read_csv_output
        # df = df.rename(columns={'surname': 'lastname'})  # Uncomment if needed
        return df
    except Exception as e:
        context.log.info(str(e))


@op(name="extract_data" , out=Out(io_manager_key="file_io"))
def extract_data(context) -> pd.DataFrame:
    """Extract Data from Postgresql."""
    conn = get_postgres_conn()
    cursor = conn.cursor()
    query = "select * FROM public.sfo_q2_weather"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    context.log.info(df.head())
    return df


@op(name="load_dim_data" , out=Out(io_manager_key="db_io"))
def load_dim_data(context, extract_sfo_q2_weather_output: pd.DataFrame) -> pd.DataFrame:
    """Transform and Stage Data into Postgres."""
    try:
        context.log.info(extract_sfo_q2_weather_output.head())
        df = extract_sfo_q2_weather_output
        df = df.rename(columns={'station': 'station_weather'})
        return df
    except Exception as e:
        context.log.info(str(e))