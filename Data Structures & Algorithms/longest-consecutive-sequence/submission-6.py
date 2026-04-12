class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longestlen = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                length = 1
                while nums[i] + length in hashset:
                    length += 1
                
                longestlen = max(longestlen, length)
        
        return longestlen


