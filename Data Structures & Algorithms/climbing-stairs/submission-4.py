class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n-1):
            tmp = one
            one = one + two # solution of last two subproblems
            two = tmp
        
        return one