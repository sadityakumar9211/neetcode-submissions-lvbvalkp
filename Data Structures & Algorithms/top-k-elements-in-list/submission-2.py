class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        freqToNums = collections.defaultdict(list)
        for num, count in counter.items():
            freqToNums[count].append(num)
        
        print(freqToNums)
        res = []
        for i in range(len(nums), -1, -1):
            if i in freqToNums:
                for j in range(len(freqToNums[i])):
                    res.append(freqToNums[i][j])
                    if len(res) == k:
                        return res
        
        return res
            
