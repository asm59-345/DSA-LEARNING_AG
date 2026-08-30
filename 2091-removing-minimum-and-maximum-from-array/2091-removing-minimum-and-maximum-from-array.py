class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = max_idx = 0
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            elif nums[i] > nums[max_idx]:
                max_idx = i

        low, high = min(min_idx, max_idx), max(min_idx, max_idx)

        
        return min(
            high + 1,              
            n - low,               
            (low + 1) + (n - high) 
        )