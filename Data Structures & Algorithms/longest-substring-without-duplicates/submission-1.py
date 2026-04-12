class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        window = {}
        ans = 0
        
        for fast, ch in enumerate(s):
            if ch in window and window[ch] >= slow:
                slow = window[ch] + 1

            window[ch] = fast
            ans = max(ans, fast - slow + 1)

        return ans
