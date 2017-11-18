class BikePost():
    def __init__(self,stationName, latitude, longitude):
        # Individual ID of the bike post
        self.stationName = stationName
        self.location = (latitude, longitude)
        self.countStarts = 0
        self.countStops = 0

    def __repr__(self):
        return "" + self.stationName + " (" + str(self.location[0]) + ", " + str(self.location[1]) + ")"