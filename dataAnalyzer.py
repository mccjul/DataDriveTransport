# coding=UTF-8
import pandas as pd
import numpy as np
import dataparser
import bikepost

class DataAnalyzer():

    def __init__(self):
        self.dataParser = dataparser
        self.bikepostList = dataparser.bikepostList
        self.bikePostsLatitudeList = []
        self.bikePostsLongitudeList = []
        self.bikePostsNameList = []

    def get_allBikePostsLatitude(self):
        for b in self.bikepostList:
            if b is not None:
                self.bikePostsLatitudeList.append(b.location[0])
        return self.bikePostsLatitudeList

    def get_allBikePostsLongitude(self):
        for b in self.bikepostList:
            if b is not None:
                self.bikePostsLongitudeList.append(b.location[1])
        return self.bikePostsLongitudeList

    def get_allBikePostsName(self):
        for b in self.bikepostList:
            if b is not None:
                self.bikePostsNameList.append(b.stationName)
        return self.bikePostsNameList
