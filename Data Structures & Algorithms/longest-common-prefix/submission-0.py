class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for col in range(len(strs[0])):
            c = strs[0][col]
            for row in range(len(strs)):
                if col >= len(strs[row]) or strs[row][col] != c:
                    return "".join(result)
            result.append(c)
        return "".join(result)