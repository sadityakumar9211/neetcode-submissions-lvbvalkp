class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = [(nums[i], i) for i in range(len(nums))]
        sortedNums.sort()

        low, high = 0, len(nums)-1
        while low < high:
            total = sortedNums[low][0] + sortedNums[high][0]
            if total == target:
                return list(sorted([sortedNums[low][1], sortedNums[high][1]]))
            elif total < target:
                low += 1
            else:
                high -= 1
