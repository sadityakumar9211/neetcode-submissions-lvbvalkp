import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k, self.stream = k, [-num for num in nums]
        heapq.heapify(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, -val)
        popped = []
        for i in range(self.k-1):
            popped.append(heapq.heappop(self.stream))
        
        ans = -self.stream[0]
        for el in popped:
            heapq.heappush(self.stream, el)
            
        return ans

