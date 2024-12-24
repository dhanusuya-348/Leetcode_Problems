class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxval = max(candies)
        for i in candies:
            i += extraCandies
            if(i >= maxval):
                ans.append(True)
            else:
                ans.append(False)
        return ans        