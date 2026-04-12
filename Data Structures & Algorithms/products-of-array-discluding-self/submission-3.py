class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)
        # Getting pre-product
        for i in range(1, len(nums)):
            results[i] = results[i-1] * nums[i-1]
        
        # Calculating post-product and combining with pre-product as well.
        postproduct = 1
        for i in range(len(nums)-2, -1, -1):
            postproduct *= nums[i+1]
            results[i] = results[i] * postproduct

        return results
