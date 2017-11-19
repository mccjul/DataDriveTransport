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

df = pd.read_csv('data/2014_04_Trips.csv')
tripList = []
# duration, startTime, endTime, startBikepost, endBikepost, userType
count = 0
for index, row in df.iterrows():
    tripList.append(trip.Trip(row['tripduration'], row['starttime'], row['stoptime'], bikepostList[int(row['start station id'])],
                              bikepostList[int(row['end station id'])], row['usertype']))
    count += 1
    if count > 100:
        break





