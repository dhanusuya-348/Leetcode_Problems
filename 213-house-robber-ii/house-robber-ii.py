class Solution(object):

    def rob(self, nums):

        # single house
        if len(nums) == 1:
            return nums[0]

        # case 1: exclude last
        case1 = self.solve(nums[:-1])

        # case 2: exclude first
        case2 = self.solve(nums[1:])

        return max(case1, case2)

    def solve(self, nums):

        n = len(nums)

        # dp array
        dp = [0] * n

        # base cases
        dp[0] = nums[0]

        if n > 1:
            dp[1] = max(nums[0], nums[1])

        # fill dp table
        for i in range(2, n):

            robcurrent = nums[i] + dp[i-2]

            skipcurrent = dp[i-1]

            dp[i] = max(robcurrent, skipcurrent)

        return dp[n-1]

# class Solution(object):
#     def rob(self, nums):
#         return self.solve(nums, 0)
    
#     def solve(self, nums, index):
#         if (index >= len(nums)):
#             return 0
#         robcurrent = nums[index] + self.solve(nums, index+2)
#         skipcurrent = self.solve(nums, index+1)
#         return max(robcurrent, skipcurrent)

# class Solution(object):
#     def rob(self, nums):
#         # single house
#         if len(nums) == 1:
#             return nums[0]
#         # case 1: exclude last
#         dp1 = [-1] * len(nums)
#         case1 = self.solve(nums[:-1], 0, dp1)
#         # case 2: exclude first
#         dp2 = [-1] * len(nums)
#         case2 = self.solve(nums[1:], 0, dp2)
#         return max(case1, case2)
#     def solve(self, nums, index, dp):
#         if index >= len(nums):
#             return 0
#         if dp[index] != -1:
#             return dp[index]
#         robcurrent = nums[index] + self.solve(nums, index+2, dp)
#         skipcurrent = self.solve(nums, index+1, dp)
#         dp[index] = max(robcurrent, skipcurrent)
#         return dp[index]