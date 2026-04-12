class Solution:
    def hasDuplicate(self, nums):
        uniqueList = set()
        for num in nums:
            if num not in uniqueList:
                uniqueList.add(num)
            else:
                # Value appears twice
                return True
        # No value appeared twice
        return False

    # Time: O(n)
    # Space: O(n)