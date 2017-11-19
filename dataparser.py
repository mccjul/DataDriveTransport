import bikepost
import trip
import pandas as pd
import numpy as np



class Dataparser():
    def __init__(self, data):
        self.dfStations = pd.read_csv('data/Stations.csv')
        self.dfRangeBikepost = self.dfStations.copy()
        self.set_dfRangeBikepost(data)

        self.matrixCustomerTrips04 = self.convertTo_matrixTrips(pd.read_csv('data/itmatrixCustomer.csv'))
        self.matrixSubscriberTrips04 = self.convertTo_matrixTrips(pd.read_csv('data/itmatrixSubscriber.csv'))

    def set_dfRangeBikepost(self, rangemap):
        lat1 = rangemap['S']
        lat2 = rangemap['N']
        lon1 = rangemap['W']
        lon2 = rangemap['E']

        self.dfRangeBikepost = self.dfRangeBikepost.query('Latitude > @lat1 and Latitude < @lat2 and Longitude > @lon1 and Longitude < @lon2')

    def convertTo_matrixTrips(self, df):
        return df.as_matrix()

    def get_allBikePostsLatitudeList(self):
        return self.dfRangeBikepost['Latitude'].values.tolist()

    def get_allBikePostsLongitudeList(self):
        return self.dfRangeBikepost['Longitude'].values.tolist()

    def get_allBikePostsNameList(self):
        return self.dfRangeBikepost['Station Name'].values.tolist()

    def get_mostPopularPath(self):
        return self.matrixCustomerTrips04.max()



data = {
    'N':40.7,
    'S':40,
    'W':-74,
    'E':-73
}

dataparser = Dataparser(data)
print(dataparser.get_mostPopularPath())



