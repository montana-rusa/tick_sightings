import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

# the dataset has no duplicates or incomplete row

#plan: have two graphs, the bar showing 

df['date'] = df['date'].str[:10]
df['date'] = pd.to_datetime(df['date']) 
print(df)