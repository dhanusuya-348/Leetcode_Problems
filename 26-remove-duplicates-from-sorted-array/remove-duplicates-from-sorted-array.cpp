class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        int j=1;
        int count=1;
        for(int i=1; i<len; i++)
        {
            if(nums[i] != nums[i-1]){
                nums[j] = nums[i];
                count++;
                j++;
            }
        }        
        return count;
    }
};