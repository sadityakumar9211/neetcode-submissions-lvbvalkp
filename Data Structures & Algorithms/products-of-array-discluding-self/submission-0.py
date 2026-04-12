class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)
        preproduct = 1
        for i in range(len(nums)):
            preproduct *= nums[i-1] if i > 0 else 1

            # Get the post product
            j = i + 1
            postproduct = 1
            while j < len(nums):
                postproduct *= nums[j]
                j += 1
            
            results[i] *= preproduct * postproduct
        
        return results