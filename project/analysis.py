import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')


# the dataset has no duplicates or incomplete row

#plan: have two graphs, the bar showing the number of sightings in each region over a set time interval, 
#a line showing sightings per month over time
df['date'] = df['date'].str[:10]
df['date'] = pd.to_datetime(df['date']) 
#print(df)


def filter_by_time(start = None, end = None, df=df):

    if start != None:
        regional = df[(df['date'] > start) & (df['date'] < end)]
    else:
        regional = df.copy()

    regional = regional.groupby(['location']).count()
    regional = regional.sort_values(by="id", ascending=False)
    
    x = regional.index.to_list()
    y = regional['id'].to_list()

    return (x, y)

def filter_by_location(location=None, df=df):

    if location == None:
        month_df = df.copy()
    else:
        month_df = df[df['location'] == location]


    month_df['year'] = month_df['date'].dt.year
    month_df['month'] = month_df['date'].dt.month
    month_df = month_df.sort_values(by=['year','month'], ascending=True).reset_index(drop=True)
    month_df = month_df.groupby(['year','month']).count()

    y = np.zeros(156) #change to reflect number of months in the time period shown by the data

    for date, count in zip(month_df.index, month_df['id']):
        y[((date[0] - 2012)*12) + date[1]-1] = count
    x = list(range(len(y)))
    y = list(y)

    return (x, y)


