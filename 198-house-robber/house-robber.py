class Solution(object):
    def rob(self, nums):
        dp = [-1] * len(nums)
        return self.solve(nums, 0, dp)

    def solve(self, nums, index, dp):
        if index >= len(nums):
            return 0
        if dp[index] != -1:
            return dp[index]
        robcurrent = nums[index] + self.solve(nums, index+2, dp)
        skipcurrent = self.solve(nums, index+1, dp)
        dp[index] = max(robcurrent, skipcurrent)
        return dp[index]


# class Solution(object):
#     def rob(self, nums):
#         return self.solve(nums, 0)
    
#     def solve(self, nums, index):
#         if (index >= len(nums)):
#             return 0
#         robcurrent = nums[index] + self.solve(nums, index+2)
#         skipcurrent = self.solve(nums, index+1)
#         return max(robcurrent, skipcurrent)
        