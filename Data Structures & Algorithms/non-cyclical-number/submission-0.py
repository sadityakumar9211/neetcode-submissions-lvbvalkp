class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            # replace with the sum of digit squares
            n = self.sumOfSquares(n)
        
        return False
    
    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        
        return res

            
            