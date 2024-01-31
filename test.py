import pandas as pd

file_path = r'./etl/sfo_q2_weather_sample.csv'
df = pd.read_csv(file_path)
print(df)