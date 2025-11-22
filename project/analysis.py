import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')


# the dataset has no duplicates or incomplete row

#plan: have two graphs, the bar showing the number of sightings in each region over a set time interval, 
#a line showing sightings per month over time
df['date'] = df['date'].str[:10]
df['date'] = pd.to_datetime(df['date']) 
print(df)


def filter_by_time(time, df=df):
    today = pd.to_datetime("today")

    if time == "week":
        cutoff = today - pd.DateOffset(weeks = 1)
    elif time == "month":
        cutoff = today - pd.DateOffset(months = 1)
    elif time == "year":
        cutoff = today - pd.DateOffset(years = 1)
    else: cutoff = False

    #print(cutoff.date())
    regional = df.groupby(['location']).count()
    print(regional)

    x = regional.index.to_list()
    y = regional['id'].to_list()

    return (x, y)

filter_by_time("year", df)



