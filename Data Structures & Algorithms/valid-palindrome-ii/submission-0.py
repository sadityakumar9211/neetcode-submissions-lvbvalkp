class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validnPalindrome(left, right, n):
            if n < 0: 
                return False
            
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return validnPalindrome(left, right-1, n-1) or validnPalindrome(left+1, right, n-1)
            
            return True
        
        return validnPalindrome(0, len(s)-1, 1)