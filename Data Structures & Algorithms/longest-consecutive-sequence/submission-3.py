class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # in-place sorting
        nums.sort()
        res, i = 1, 1
        
        while i < len(nums):
            length = 1
            while i < len(nums) and nums[i] <= 1 + nums[i-1]:
                length += nums[i] - nums[i-1]
                i += 1
            
            res = max(res, length)
            i += 1
    
        return res


