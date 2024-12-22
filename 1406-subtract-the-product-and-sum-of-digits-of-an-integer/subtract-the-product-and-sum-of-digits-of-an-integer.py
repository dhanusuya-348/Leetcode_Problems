class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        result = 0
        strval = str(n)
        for i in strval:
            product *= int(i)
            sum += int(i)
        result = product - sum
        return result