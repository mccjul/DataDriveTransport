import math

class Trip():
    def __init__(self, duration, startTime, endTime, startBikepost, endBikepost, userType):

        # Initiate Attributes
        self.duration = duration
        self.startTime = startTime
        self.endTime = endTime
        self.startBikepost = startBikepost
        self.endBikepost = endBikepost
        self.userType = userType
        self.isOvertimed = False

        # Overtime variable
        self.durationOvertime = 0
        self.intervalOvertime = 0

        # Initial Triggers
        if userType == "Customer" and self.duration > 1800:
            self.isOvertimed = True
            self.durationOvertime = self.duration - 1800
            self.intervalOvertime = math.ceil(self.duration/1800)
        elif userType == "Subscriber" and duration > 2700:
            self.isOvertimed = True
            self.durationOvertime = self.duration - 2700
            self.intervalOvertime = math.ceil(self.duration / 2700)

