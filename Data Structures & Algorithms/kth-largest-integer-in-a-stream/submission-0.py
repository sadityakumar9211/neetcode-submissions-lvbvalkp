class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.stream = k, sorted(nums)

    def add(self, val: int) -> int:
        import bisect
        insertionIndex = bisect.bisect_left(self.stream, val)
        self.stream = self.stream[:insertionIndex] + [val] + self.stream[insertionIndex:]
        return self.stream[-self.k]
        
