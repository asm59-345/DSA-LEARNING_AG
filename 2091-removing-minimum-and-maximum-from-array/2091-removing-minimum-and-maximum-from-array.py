class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n<= 2:
            return n
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        low  = min(min_idx, max_idx)
        high = max(min_idx, max_idx)

        o1= high +1
        o2 = n - low
        o3 = (low +1 ) + (n - high)

        return min(o1,o2,o3)