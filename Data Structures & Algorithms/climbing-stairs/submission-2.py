class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return int(i == n)
            return dfs(i+1) + dfs(i+2) # solving subproblems
        
        return dfs(0)