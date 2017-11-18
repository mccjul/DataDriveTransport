import bikepost
import trip
import pandas as pd
import numpy as np

# Parse memberships

# Parse bikeposts
bf = pd.read_csv('data/Stations.csv')
bikepostList = [None]*3005

for index, row in bf.iterrows():
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





