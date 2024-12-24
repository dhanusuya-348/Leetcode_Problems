class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        new_num = int(num[::-1])
        num2 =  str(new_num)
        num = num2[::-1]
        return num
        

        