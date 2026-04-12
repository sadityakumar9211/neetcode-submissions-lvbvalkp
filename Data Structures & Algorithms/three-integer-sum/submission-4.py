class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        print(nums)
        res = set()
        for i in range(n):
            target = -nums[i]
            left, right = i+1, n-1
            while left < right:
                total  = nums[left] + nums[right]
                if total == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return [list(el) for el in res]
