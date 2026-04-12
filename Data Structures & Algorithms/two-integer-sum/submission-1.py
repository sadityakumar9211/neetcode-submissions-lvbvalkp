class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # Find another element which completes this nums[i]
            # Since we only need combination 
            # 2, 3, 4, 5, 6, 11, 9, t = 10 => [2, 4]
            previousMap = dict()
            for i, num in enumerate(nums):
                if target - num in previousMap:
                    return [previousMap[target-num], i]
                previousMap[num] = i




