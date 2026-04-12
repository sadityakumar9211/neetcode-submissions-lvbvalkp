class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        deque = collections.deque()
        carry = 1
        for i in range(len(digits)):
            digit_sum = digits[-i-1] + carry
            deque.appendleft(digit_sum % 10)
            carry = digit_sum // 10
        
        if carry:
            deque.appendleft(carry)
        
        return list(deque)
            
