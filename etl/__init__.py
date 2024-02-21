from dagster import Definitions, load_assets_from_modules
from dagstermill import local_output_notebook_io_manager

from etl.assets import assets_module
from .io import file_io, db_io_manager
from etl.schedules import every_weekday_9am , every_minute
from etl.jobs import run_job , churn_modelling_pipeline
all_assets = load_assets_from_modules([assets_module])

defs = Definitions(
    assets=all_assets,
    jobs=[run_job],
    schedules=[every_weekday_9am],
    resources={
        "file_io": file_io.LocalFileSystemIOManager(),
         "output_notebook_io_manager": local_output_notebook_io_manager,
        "db_io": db_io_manager.postgres_pandas_io_manager.configured(
                {
                "server": {"env": "server"},
                "db": {"env": "db"},
                "uid": {"env": "uid"},
                "pwd": {"env": "pwd"},
                "port": {"env": "port"},
            }
        
         ),

    }
)

