from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return False if (len(s) != len(t) or Counter(s) != Counter(t)) else True
        if len(s) != len(t):
            return False

        count_s, count_t = Counter(s), Counter(t)

        return False if count_s != count_t else True

        
        