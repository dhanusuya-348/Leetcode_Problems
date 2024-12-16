class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int size = nums.size();
        int sum=0;
        int missNum=0;
        int total_sum=0;
        for(int i=0;i<size;i++){
            sum+=nums[i];
        }
        total_sum = (size*(size+1))/2;
        missNum = total_sum-sum;
        return missNum;
    }
};