class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combinedList = zip(names, heights)
        sortedL = sorted(combinedList, key = lambda x:x[1], reverse=True)
        ans = []
        for name, height in sortedL:
            ans.append(name)
        return ans



