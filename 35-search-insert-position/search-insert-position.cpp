class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        int count = 0;
        for(int i=0; i<len; i++){
            if(nums[i] >= target){
                return i;
            }
            count++;
        }
        return count;
    }
};