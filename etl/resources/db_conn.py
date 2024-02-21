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


