class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for index, value in enumerate(sorted(nums)):
            if value not in d:
                d[value] = index
        
        result = []
        for value in nums:
            result.append(d[value])  
        return result
