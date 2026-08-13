class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        left = 1
        right = 1
        
        for i in range(n):
            # Left se product build kar rahe hain
            res[i] *= left
            left *= nums[i]
            
            # Right se product build kar rahe hain
            res[n - 1 - i] *= right
            right *= nums[n - 1 - i]
            
        return res