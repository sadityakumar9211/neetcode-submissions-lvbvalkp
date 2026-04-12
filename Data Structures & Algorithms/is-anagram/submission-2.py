from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = defaultdict(int), defaultdict(int)

        for ch in s:
            count_s[ch] += 1
        for ch in t:
            count_t[ch] += 1
        
        return True if count_s.__eq__(count_t) else False

        

        