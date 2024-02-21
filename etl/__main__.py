"""Example of how to run a Dagster op from normal Python script."""
from etl.jobs import run_job

if __name__ == "__main__":
    result = run_job.execute_in_process()