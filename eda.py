# Exploratory Data Analysis Script
import pandas as pd

data = 'weatherAUS.csv'
df = pd.read_csv(data)

print(df.shape)
