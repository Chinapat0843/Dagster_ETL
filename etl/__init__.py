from dagster import Definitions, load_assets_from_modules

from etl.assets.extract import extract_local_file 
from etl.assets.load import load
from etl.assets.transform import transform

from .io import file_io, db_io_manager
#from etl.schedules import every_minute
#from etl.jobs import run_job 

all_assets = load_assets_from_modules([extract_local_file , transform , load])

defs = Definitions(
    assets=all_assets,
    #jobs=[run_job],
    #schedules=[every_minute],
    resources={
        "file_io": file_io.LocalFileSystemIOManager(),
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

