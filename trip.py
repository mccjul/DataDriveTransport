__author__ = Kevin

class Trip():
    def __init__(self, startBikepost, endBikepost):
        self.duration = 0
        self.startTime = 0
        self.endTime = 0
        self.startBikepost = startBikepost
        self.endBikepost = endBikepost
        self.userType = ""
        self.birthyear = 0
        # Gender = 0 is unknown; 1 is male; 2 is female;
        self.gender = 0