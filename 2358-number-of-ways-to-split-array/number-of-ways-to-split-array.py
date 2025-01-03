class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        totalsum = sum(nums)
        sum1=0
        for i in range(len(nums)-1):
            sum1 += nums[i]
            sum2 = totalsum - sum1
            if(sum1>=sum2):
                ans += 1
        return ans
            

        