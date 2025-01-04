class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()

        for i in range(26):  # Loop over each letter 'a' to 'z'
            char = chr(i + ord('a'))
            first = s.find(char)  # Find the first occurrence of char
            last = s.rfind(char)  # Find the last occurrence of char

            if first != -1 and last != -1 and first < last:
                # Get the characters between the first and last occurrence
                middle_chars = set(s[first + 1:last])
                # Add all unique palindromic subsequences of form 'a_b_a'
                for mid_char in middle_chars:
                    result.add((char, mid_char, char))

        return len(result)
