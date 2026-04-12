class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquare(n)
        while slow != fast:
            fast = self.sumOfSquare(self.sumOfSquare(fast))
            slow = self.sumOfSquare(slow)
    
        return True if slow == 1 else False
    

    def sumOfSquare(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
            
        return res