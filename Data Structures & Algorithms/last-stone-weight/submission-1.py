import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-weight for weight in stones]
        heapq.heapify(stoneHeap)

        while len(stoneHeap) > 1:
            x, y = heapq.heappop(stoneHeap), heapq.heappop(stoneHeap)
            if x != y:
                heapq.heappush(stoneHeap, -abs(x-y))
        
        return -stoneHeap[0] if stoneHeap else 0