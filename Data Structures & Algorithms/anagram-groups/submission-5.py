class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for str in strs:
            cur_str = [0] * 26

            for char in str:
                index = ord(char) - ord('a')
                cur_str[index] += 1
            
            output[tuple(cur_str)].append(str)

        return list(output.values())
            
