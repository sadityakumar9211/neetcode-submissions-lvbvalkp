class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(n) = min(f(n-1) + cost[n-1], f(n-2) + cost[n-2])
        # f(0) = f(1) = 0

        first, second = 0, 0
        for i in range(2, len(cost)+1):
            tmp = second
            second = min(second + cost[i-1], first + cost[i-2])
            first = tmp
        
        return second
        