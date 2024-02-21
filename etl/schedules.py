from dagster import ScheduleDefinition
from etl.jobs import run_job , churn_modelling_pipeline


every_weekday_9am = ScheduleDefinition(
    name = "job1",
    job=run_job,
    cron_schedule="* * * * *",
    execution_timezone="Asia/Bangkok",
)

every_minute = ScheduleDefinition(
    name = "job2",
    job=churn_modelling_pipeline,
    cron_schedule="* * * * *",
    execution_timezone="Asia/Bangkok",
)