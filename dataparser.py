import bikepost
import trip
import pandas as pd
import numpy as np

class Dataparser():
    def __init__(self, data):
        self.dfStations = pd.read_csv('data/Stations.csv')
        self.dfRangeBikepost = self.dfStations.copy()
        self.set_dfRangeBikepost(data)

        self.dfTrips04 = pd.read_csv('data/2014_04_Trips.csv')
        self.dfMostPopularCustomerPaths = self.dfTrips04.copy()
        self.dfMostPopularSubscriberPaths = self.dfTrips04.copy()
        self.set_mostPopularPaths()

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

    def set_mostPopularPaths(self):
        bikepostRangeList = self.dfRangeBikepost['Station ID'].values.tolist()

        self.dfMostPopularCustomerPaths = self.dfMostPopularCustomerPaths\
            .query('usertype == "Customer" and startstationid in @bikepostRangeList and endstationid in @bikepostRangeList')\
            .groupby(['startstationid', 'endstationid'])\
            .size().reset_index(name='count').sort_values(by='count', ascending=False)

        self.dfMostPopularSubscriberPaths = self.dfMostPopularSubscriberPaths\
            .query('usertype == "Subscriber" and startstationid in @bikepostRangeList and endstationid in @bikepostRangeList')\
            .groupby(['startstationid', 'endstationid'])\
            .size().reset_index(name='count').sort_values(by='count', ascending=False)

    def get_mostPopularCustomerPathList(self, count):
        mostPopularCustomerPathList = []
        for p in range(count):
            mostPopularCustomerPathList.append(self.dfMostPopularCustomerPaths['startstationid'].values.tolist()[p])
        return mostPopularCustomerPathList

    def get_mostPopularCustomerPathCountList(self, count):
        mostPopularCustomerPathCountList = []
        for p in range(count):
            mostPopularCustomerPathCountList.append(self.dfMostPopularCustomerPaths['count'].values.tolist()[p])
        return mostPopularCustomerPathCountList

    def get_mostPopularSubscriberPathList(self, count):
        mostPopularSubscriberPathList = []
        for p in range(count):
            mostPopularSubscriberPathList.append(self.dfMostPopularSubscriberPaths['startstationid'].values.tolist()[p])
        return mostPopularSubscriberPathList

    def get_mostPopularSubscriberPathCountList(self, count):
        mostPopularSubscriberPathCountList = []
        for p in range(count):
            mostPopularSubscriberPathCountList.append(self.dfMostPopularSubscriberPaths['count'].values.tolist()[p])
        return mostPopularSubscriberPathCountList




data = {
    'N':40.7,
    'S':40,
    'W':-74,
    'E':-73
}

dataparser = Dataparser(data)
print(dataparser.get_mostPopularSubscriberPathList(5))
print(dataparser.get_mostPopularSubscriberPathCountList(5))



