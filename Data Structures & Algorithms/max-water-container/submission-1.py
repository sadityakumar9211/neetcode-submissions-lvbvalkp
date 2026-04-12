class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            res = max(res, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res

        # We can deterministically decrease the window (because the max capacity 
        # is limited by the small of the two bars and hence moving the smaller line is 
        # the only option to get to a bigger container).
        # Since we want to maximize the size, so we can use the two pointers approach here.
        