class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = sorted(nums)
        for i in range(1, len(lst)):
            if lst[i-1] == lst[i]:
                return lst[i-1]
        
        
