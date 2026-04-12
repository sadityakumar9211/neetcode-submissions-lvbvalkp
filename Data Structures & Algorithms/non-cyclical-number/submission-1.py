class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            
            visited.add(n)
            n = self.sumOfSquare(n)
            
        return False

    def sumOfSquare(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
            
        return res
