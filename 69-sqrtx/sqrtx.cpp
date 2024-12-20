class Solution {
public:
    int mySqrt(int x) {
        int low=1;
        long high=x;
        long mid=0;
        while(low<=high){
            //mid = low+((high-low)/2);
            mid = (low+high)/2;
            if((mid*mid)<x){
                low=mid+1;
            }
            else if((mid*mid)>x){
                high=mid-1;
            }
            else{
                return mid;
            }
        }
        return (int)high;
    }
};