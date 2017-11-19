# coding=UTF-8
import pandas as pd
import numpy as np
import dataparser
import bikepost

class DataAnalyzer():

    def __init__(self):
        self.dataParser = dataparser
        self.bikepostList = dataparser.bikepostList
        self.tripList = dataparser.tripList
        self.pathList = []
        self.get_allPaths()

    def get_allBikePostsLatitude(self):
        bikePostsLatitudeList = []
        for b in self.bikepostList:
            if b is not None:
                bikePostsLatitudeList.append(b.location[0])
        return bikePostsLatitudeList

    def get_allBikePostsLongitude(self):
        bikePostsLongitudeList = []
        for b in self.bikepostList:
            if b is not None:
                bikePostsLongitudeList.append(b.location[1])
        return bikePostsLongitudeList

    def get_allBikePostsName(self):
        bikePostsNameList = []
        for b in self.bikepostList:
            if b is not None:
                bikePostsNameList.append(b.stationName)
        return bikePostsNameList

    def get_allPaths(self):
        count = 0
        for t in self.tripList:
            self.pathList.append((t.startBikepost, t.endBikepost))
        return self.pathList

    def get_allLatitudePaths(self):
        #startLatitude, endLatitude
        allStartLat = []
        allEndLat = []
        allLatitudePaths = (allStartLat, allEndLat)
        count =0
        for p in self.pathList:
            allLatitudePaths[0].append(p[0].location[0])
            allLatitudePaths[1].append(p[1].location[0])
        return allLatitudePaths

    def get_allLongitudePaths(self):
        allStartLon = []
        allEndLon = []
        allLongitudePaths = (allStartLon, allEndLon)
        for p in self.pathList:
            allLongitudePaths[0].append(p[0].location[1])
            allLongitudePaths[0].append(p[0].location[1])
        return allLongitudePaths

