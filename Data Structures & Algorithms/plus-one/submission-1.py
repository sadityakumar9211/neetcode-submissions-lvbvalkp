class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            digit_sum = digits[-i-1] + carry
            digits[-i-1] = digit_sum % 10
            carry = digit_sum // 10
        
        if carry:
            digits = [carry] + digits
        
        return digits
            
