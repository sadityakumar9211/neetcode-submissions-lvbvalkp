class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        deque = collections.deque([])
        carry = 1
        for i in range(len(digits)):
            _sum = digits[-i-1] + carry
            deque.appendleft(_sum % 10)
            carry = _sum // 10
        
        if carry:
            deque.appendleft(carry)
        return list(deque)
            