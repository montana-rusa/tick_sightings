import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')


# the dataset has no duplicates or incomplete row

#plan: have two graphs, the bar showing the number of sightings in each region over a set time interval, 
#a line showing sightings per month over time
df['date'] = df['date'].str[:10]
df['date'] = pd.to_datetime(df['date']) 
#print(df)


def filter_by_time(start = False, end = False, df=df):

    if start != False:
        regional = df[(df['date'] > start) & (df['date'] < end)]
    else:
        regional = df
   
    #print(cutoff.date())
    regional = df.groupby(['location']).count()
    regional = regional.sort_values(by="id", ascending=False)
    #print(regional)



    x = regional.index.to_list()
    y = regional['id'].to_list()

    return (x, y)


