class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(ch: str) -> bool:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
                return True
            else:
                return False

        first, second = 0, len(s)-1
        while first < second:
            if not isAlphanumeric(s[first]):
                first += 1
                continue
            if not isAlphanumeric(s[second]):
                second -= 1
                continue

            # If both alphanumeric characters but not equal
            if first < second and s[first].lower() != s[second].lower():
                return False

            first += 1
            second -= 1
            
        return True