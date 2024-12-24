class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        totalTime = arrivalTime + delayedTime
        if (totalTime == 24):
            return 0
        elif (totalTime < 24):
            return totalTime
        else:
            return (totalTime - 24)
        