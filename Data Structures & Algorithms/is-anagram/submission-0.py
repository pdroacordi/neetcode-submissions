class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        must_have = [0] * 26
        occ       = [0] * 26

        for ch in s:
            must_have[ord(ch) - ord('a')] += 1
        
        for ch in t:
            occ[ord(ch) - ord('a')] += 1
        
        return must_have == occ