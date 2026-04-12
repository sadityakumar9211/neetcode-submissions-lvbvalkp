class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums) # To look for elements in O(1) time.
        longest = 0

        for i in range(len(nums)):
            # If n-1th element is not present, then found a start of the seq.
            if (nums[i] - 1) not in hashset:
                length = 1
                while (nums[i] + length)  in hashset:
                    length += 1
                
                longest = max(longest, length)
        
        return longest

        