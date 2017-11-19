import bikepost
import trip
import pandas as pd
import numpy as np

class Dataparser():
    def __init__(self, rangemap):
        self.dfStations = pd.read_csv('data/Stations.csv')
        self.dfRangeBikepost = self.dfStations.copy()
        self.set_dfRangeBikepost(rangemap)

        self.dfTrips = pd.read_csv('data/2014_04_Trips.csv')
        self.dfMostPopularCustomerPaths = self.dfTrips.copy()
        self.dfMostPopularSubscriberPaths = self.dfTrips.copy()
        self.set_mostPopularPaths()

    def set_month(self, month):
        self.dfTrips = pd.read_csv('data/2014_0'+str(month)+'_Trips.csv')

    def set_dfRangeBikepost(self, rangemap):
        lat1 = rangemap['S']
        lat2 = rangemap['N']
        lon1 = rangemap['W']
        lon2 = rangemap['E']

        self.dfRangeBikepost = self.dfRangeBikepost.query('Latitude > @lat1 and Latitude < @lat2 and Longitude > @lon1 and Longitude < @lon2')

    def get_allBikePostsLatitudeList(self):
        return self.dfRangeBikepost['Latitude'].values.tolist()

    def get_allBikePostsLongitudeList(self):
        return self.dfRangeBikepost['Longitude'].values.tolist()

    def get_allBikePostsNameList(self):
        return self.dfRangeBikepost['StationName'].values.tolist()

    def set_mostPopularPaths(self):
        bikepostRangeList = self.dfRangeBikepost['StationID'].values.tolist()

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
        mostPopularCustomerPathNameList = []
        for p in range(count):
            mostPopularCustomerPathList.append(self.dfMostPopularCustomerPaths['startstationid'].values.tolist()[p])
            mostPopularCustomerPathNameList = \
            self.dfRangeBikepost.query('StationID in @mostPopularCustomerPathList')['StationName'].values.tolist()
        return mostPopularCustomerPathNameList

    def get_mostPopularCustomerPathCountList(self, count):
        mostPopularCustomerPathCountList = []
        for p in range(count):
            mostPopularCustomerPathCountList.append(self.dfMostPopularCustomerPaths['count'].values.tolist()[p])
        return mostPopularCustomerPathCountList

    def get_mostPopularSubscriberPathList(self, count):
        mostPopularSubscriberPathList = []
        mostPopularSubscriberPathNameList = []
        for p in range(count):
            mostPopularSubscriberPathList.append(self.dfMostPopularSubscriberPaths['startstationid'].values.tolist()[p])
            mostPopularSubscriberPathNameList = self.dfRangeBikepost.query('StationID in @mostPopularSubscriberPathList')['StationName'].values.tolist()
        return mostPopularSubscriberPathNameList

    def get_mostPopularSubscriberPathCountList(self, count):
        mostPopularSubscriberPathCountList = []
        for p in range(count):
            mostPopularSubscriberPathCountList.append(self.dfMostPopularSubscriberPaths['count'].values.tolist()[p])
        return mostPopularSubscriberPathCountList

    def get_mostPopularSubscriberPathLatitudeList(self, count):
        mostPopularSubscriberPathList = []
        mostPopularSubscriberPathLatitudeList = []
        for p in range(count):
            mostPopularSubscriberPathList.append(self.dfMostPopularSubscriberPaths['startstationid'].values.tolist()[p])
            mostPopularSubscriberPathLatitudeList = \
            self.dfRangeBikepost.query('StationID in @mostPopularSubscriberPathList')['Latitude'].values.tolist()
        return mostPopularSubscriberPathLatitudeList







