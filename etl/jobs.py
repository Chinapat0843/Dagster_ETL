
from etl.assets import assets_module
from etl.ops import ops
from dagster import (
    define_asset_job,
    AssetSelection,
    job
)

# define jobs as selections over the larger graph
run_job = define_asset_job("run_job", AssetSelection.groups("churn_modelling"))

@job(name="churn_modelling_job")
def churn_modelling_pipeline():
    read_csv_output = ops.read_csv_file()
    ops.load_data(read_csv_output=read_csv_output)

    extract_output = ops.extract_data()
    ops.load_dim_data(extract_sfo_q2_weather_output=extract_output)
