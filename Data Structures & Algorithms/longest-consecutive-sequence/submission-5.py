class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashset = set(nums)

        for i in range(len(nums)):
            # Find the starting point of each sequence.
            if (nums[i] - 1) not in hashset:
                # For each starting point of the sequence.
                length = 1
                while (nums[i] + length) in hashset:
                    length += 1
                
                longest = max(longest, length)
        
        return longest