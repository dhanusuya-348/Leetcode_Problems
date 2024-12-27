class Solution:
    def addDigits(self, num: int) -> int:
        sumN = num
        if(num < 10):
            return num
        while(sumN > 9):
            ans = 0
            for i in str(sumN):
                ans += int(i)
            sumN = ans
        return sumN
        
        