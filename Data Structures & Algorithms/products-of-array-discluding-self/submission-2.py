class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)

        # Only calculating and storing preproducts for each position
        for i in range(1, len(nums)):
            results[i] = results[i-1] * nums[i-1]
        
        [1, 2, 4, 6]
        [1, 1, 2, 8]
        # Now calculating the postproducts for each position as well
        # and combining
        postproduct = 1
        for i in range(len(nums)-2, -1, -1):
            postproduct *= nums[i+1]
            results[i] = results[i] * postproduct  # preproduct * postproduct
        
        return results

# Time: O(n)
# Space: O(1)
