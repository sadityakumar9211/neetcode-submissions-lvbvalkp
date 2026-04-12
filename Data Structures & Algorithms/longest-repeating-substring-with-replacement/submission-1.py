class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        left, ans = 0, 0
        for right in range(len(s)):
            freq[s[right]] += 1
            size = right - left + 1
            while size - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
                size = right - left + 1
            ans = max(ans, size)
        return ans