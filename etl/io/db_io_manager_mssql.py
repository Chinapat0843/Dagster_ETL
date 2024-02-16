import json

import pandas as pd
from sqlalchemy import create_engine

from dagster import (
    Field,
    IOManager,
    InitResourceContext,
    InputContext,
    OutputContext,
    StringSource,
    io_manager,
)


class MSSQLDataframeIOManager(IOManager):
    def __init__(self, driver: str, uid: str, pwd: str, server: str, db: str, port: str):
        # Add driver parameter for connecting to MSSQL
        self.driver = driver
        self.uid = uid
        self.pwd = pwd
        self.db = db
        self.server = server
        self.port = port

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        if obj is None:
            return

        table_name = context.asset_key.to_python_identifier()
        engine = create_engine(
            f"{self.driver}://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}"
        )
        obj.to_sql(table_name, engine, if_exists="replace", index=False)

        # Recording metadata from an I/O manager
        context.add_output_metadata({"db": self.db, "table_name": table_name})

    def load_input(self, context: InputContext):
        table_name = context.upstream_output.asset_key.to_python_identifier()
        engine = create_engine(
            f"{self.driver}://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}"
        )
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        return df


@io_manager(
    config_schema={
        "driver": StringSource,
        "uid": StringSource,
        "pwd": StringSource,
        "server": StringSource,
        "db": StringSource,
        "port": StringSource,
    }
)
def mssql_pandas_io_manager(init_context: InitResourceContext) -> MSSQLDataframeIOManager:
    # Update driver and config parameter names
    return MSSQLDataframeIOManager(
        driver=init_context.resource_config["driver"],
        pwd=init_context.resource_config["pwd"],
        uid=init_context.resource_config["uid"],
        server=init_context.resource_config["server"],
        db=init_context.resource_config["db"],
        port=init_context.resource_config["port"],
    )