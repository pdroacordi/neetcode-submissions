class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen  = {}
        major = 0
        most  = 0
        for i in range(len(nums)):
            app = seen.get(nums[i], 0) + 1
            seen[nums[i]] = app
            if app > most:
                major = nums[i]
                most = app
        
        return major
        
