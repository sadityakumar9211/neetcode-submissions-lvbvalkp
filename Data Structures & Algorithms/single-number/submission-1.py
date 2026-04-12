class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countMap = collections.defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        for k, v in countMap.items():
            if v == 1:
                return k
