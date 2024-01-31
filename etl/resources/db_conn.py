import os
import urllib
import pyodbc
from sqlalchemy import create_engine
from dagster import resource
import psycopg2
#
def get_postgres_conn():
    

# Establish a connection to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="password",
            host="pg-warehouse",
            port="5432",
            database="postgres"
        )

        # Create a cursor to perform database operations
        cursor = conn.cursor()

        # Example: Execute a SQL query
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("PostgreSQL Database Version:", db_version)

        # Close the cursor and connection
        cursor.close()
        return conn
        

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)



def get_sql_conn():
    """return db connection."""
    #get password from environmnet var
    pwd = os.environ['PGPASS']
    uid = os.environ['PGUID']
    #
    conn = pyodbc.connect(
              'DRIVER=' + 'ODBC Driver 17 for SQL Server' +
              ';server=' + 'localhost' +
              ';database=' + 'AdventureWorksDW2019' +
              ';UID=' + uid +
              ';PWD=' + pwd
              )
    try:
        return conn
    except:
        print("Error connecting to SQL Server")

