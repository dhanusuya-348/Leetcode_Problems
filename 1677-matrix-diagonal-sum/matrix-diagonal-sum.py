class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
            if (i != len(mat)-i-1):
                s += mat[i][len(mat)-i-1]
        return s


        