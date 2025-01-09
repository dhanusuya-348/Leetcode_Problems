class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_size = len(pref)
        count = 0
        for i in words:
            if i[:pref_size] == pref:
                count += 1
            else:
                pass
        return count
        