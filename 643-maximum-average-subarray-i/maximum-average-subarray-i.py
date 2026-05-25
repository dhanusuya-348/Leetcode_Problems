class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = len(nums)-1
        window_sum = sum(nums[left:left+k])
        avg = window_sum/float(k)
        result = avg
        left += 1
        while (left+k-1 <= right):
            window_sum = window_sum - nums[left-1] + nums[left+k-1]
            avg = window_sum/float(k)
            result = max(result, avg)
            left += 1
        return result

        