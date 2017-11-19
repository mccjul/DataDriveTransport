import bikepost
import trip
import pandas as pd
import numpy as np

# Parse memberships

# Parse bikeposts
df = pd.read_csv('data/Stations.csv')
bikepostList = [None]*3005

for index, row in df.iterrows():
    bikepostList[row['Station ID']] = bikepost.BikePost(row['Station Name'], row['Latitude'], row['Longitude'])


df = pd.read_csv('data/2014_04_Trips.csv')

class Dataparser():
    def __init__(self):
        self.f





