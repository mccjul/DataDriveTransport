import bikepost
import trip
import pandas as pd
import numpy as np

class Path():
    def __init__(self, startBikepost, endBikepost, count):
        self.startBikepost = startBikepost
        self.endBikepost = endBikepost
        self.count = count

# Parse memberships

# Parse bikeposts
df = pd.read_csv('data/Stations.csv')
bikepostList = [None]*3005

for index, row in df.iterrows():
    bikepostList[row['Station ID']] = bikepost.BikePost(row['Station Name'], row['Latitude'], row['Longitude'])

# Test
print(len(bikepostList))
print(bikepostList[3002])

# Parse trips

#Initialize Variables
totalNumberTrips = 0
totalDuration = 0

# Create trip object
totalNumberTrips += 1
totalDuration += 0 # Certain data

df = pd.read_csv('data/2014_04_Paths.csv')
pathList = []

for index, row in df.iterrows():
    pathList.append(Path(bikepostList[(int(row['start station id']))], bikepostList[(int(row['end station id']))], row['CountOfID']))







