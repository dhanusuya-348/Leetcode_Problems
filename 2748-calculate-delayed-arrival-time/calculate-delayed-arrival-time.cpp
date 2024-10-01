class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int reachingTime = arrivalTime + delayedTime;
        int value;

        if(reachingTime < 24)
        {
            value = reachingTime;
        }
        else if(reachingTime == 24)
        {
            value = 0;
        }
        else if(reachingTime > 24){
            value = reachingTime - 24;
        }
        return value;
    }
};