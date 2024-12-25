class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedArr = sorted(nums)
        dictArr = {}
        for i, val in enumerate(sortedArr):
            if val not in dictArr:
                dictArr[val] = i
        ans = []
        for j in nums:
            ans.append(dictArr[j])
        return ans

                
