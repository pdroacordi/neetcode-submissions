class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            missing = target - n
            if missing in seen:
                return [seen[missing], i]
            seen[n] = i
        return []
