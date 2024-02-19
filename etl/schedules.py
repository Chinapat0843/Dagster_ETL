from dagster import ScheduleDefinition
from etl.jobs import run_job


every_weekday_9am = ScheduleDefinition(
    job=run_job,
    cron_schedule="* * * * *",
    execution_timezone="Asia/Bangkok",
)