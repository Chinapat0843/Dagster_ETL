
from etl import assets_module
from dagster import (
    define_asset_job,
    AssetSelection
)

# define jobs as selections over the larger graph
run_job = define_asset_job("run_jupyter_job", AssetSelection.groups("churn_modelling"))
