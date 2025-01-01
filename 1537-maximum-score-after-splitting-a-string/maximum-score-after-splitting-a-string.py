class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        
        # Iterate over all possible splits (except splitting at the last character)
        for i in range(1, len(s)):
            left = s[:i]    # Left part of the string
            right = s[i:]   # Right part of the string
            
            # Calculate the score for this split
            count_zeros = left.count("0")
            count_ones = right.count("1")
            score = count_zeros + count_ones
            
            # Update the maximum score
            max_score = max(max_score, score)
        
        return max_score
