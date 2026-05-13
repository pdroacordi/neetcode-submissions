class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        gone   = set()
        for i in range(len(strs)):
            if strs[i] in gone:
                continue
            
            must_have = [0] * 26
            for ch in strs[i]:
                must_have[ord(ch) - ord('a')] += 1

            angs = []
            for j in range(len(strs)):
                seen = [0] * 26
                for ch in strs[j]:
                    seen[ord(ch) - ord('a')] += 1
                if seen == must_have:
                    angs.append(strs[j])
                    gone.add(strs[j])
            
            output.append(angs)
        return output
            
