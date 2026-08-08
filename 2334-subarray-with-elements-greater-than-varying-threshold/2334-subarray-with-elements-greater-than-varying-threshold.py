class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n   # PSE indices
        right = [n] * n   # NSE indices
        
        # Monotonic stack for Previous Smaller Element
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        # Monotonic stack for Next Smaller Element
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        # Check maximum subarray size for each nums[i] as the minimum
        for i in range(n):
            k = right[i] - left[i] - 1
            if nums[i] * k > threshold:
                return k
                
        return -1