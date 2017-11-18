__author__ = Kevin

class Trip():
    def __init__(self, duration, startTime, endTime, startBikepost, endBikepost, userType, birthyear, gender):
        # Initial Variables
        self.duration = duration
        self.startTime = startTime
        self.endTime = endTime
        self.startBikepost = startBikepost
        self.endBikepost = endBikepost
        self.userType = userType
        self.birthyear = birthyear
        # Gender = 0 is unknown; 1 is male; 2 is female;
        self.gender = gender
        self.isOvertimed = False
        self.durationOvertime = 0

        # Initial Triggers
        if userType == "Customer" and self.duration > 1800:
            self.isOvertimed = True
            self.durationOvertime = self.duration - 1800
        elif userType == "Subscriber" and duration > 2700:
            self.isOvertimed = True
            self.durationOvertime = self.duration - 2700