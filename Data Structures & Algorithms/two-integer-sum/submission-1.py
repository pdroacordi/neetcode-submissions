class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        missing = {}

        for i in range (len(nums)):
            print(nums[i], target - nums[i], i, missing)
            if (target - nums[i]) in missing:
                return [missing[target - nums[i]], i]
            missing[nums[i]] = i
        return []
