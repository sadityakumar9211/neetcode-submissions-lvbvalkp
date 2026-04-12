class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            found = False
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    found = True
                    break

            if not found:
                return nums[i]
