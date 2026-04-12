class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax, rightmax = [0] * n, [0] * n  # height can never be negative

        for i in range(1, n):
            leftmax[i] = max(height[i-1], leftmax[i-1])
        
        for i in range(n-2, -1, -1):
            rightmax[i] = max(height[i+1], rightmax[i+1])
        
        ans = 0
        for i in range(1, n-1):
            diff = min(leftmax[i], rightmax[i]) - height[i]
            if diff > 0:
                ans += diff
        
        return ans

