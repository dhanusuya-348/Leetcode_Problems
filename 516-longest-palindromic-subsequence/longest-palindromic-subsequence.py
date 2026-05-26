class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[left][right]
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.solve(0, n-1, s, dp)

    def solve(self, left, right, s, dp):
        # base cases
        if left > right:
            return 0
        if left == right:
            return 1
        # already computed
        if dp[left][right] != -1:
            return dp[left][right]
        # matching characters
        if s[left] == s[right]:
            dp[left][right] = 2 + self.solve(left+1, right-1, s, dp)
        # non-matching characters
        else:
            dp[left][right] = max(
                self.solve(left, right-1, s, dp),
                self.solve(left+1, right, s, dp)
            )
        return dp[left][right]

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:

#         left = 0
#         right = len(s)-1
#         return self.solve(left, right, s)
        
#     def solve(self, left, right, s):
        
#         if (left>right):
#             return 0
#         if(left == right):
#             return 1
#         if (s[left]==s[right]):
#             return 2 + self.solve(left+1, right-1, s)
#         elif (s[left] != s[right]):
#             return max(self.solve(left, right-1, s), self.solve(left+1, right, s))