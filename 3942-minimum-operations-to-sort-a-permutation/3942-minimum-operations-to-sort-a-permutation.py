class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        asc_count = 0
        dsc_count = 0
        
        for i in range(1, n):
            if nums[i] == (nums[i - 1] + 1) % n:
                asc_count += 1
            if nums[i - 1] == (nums[i] + 1) % n:
                dsc_count += 1
                
        if asc_count == n - 1 and nums[0] == 0:
            return 0
            
        if asc_count == n - 1:
            left_rot = n - nums[0]
            right_rot = 1 + (nums[-1] + 1) + 1
            return min(left_rot, right_rot)
            
        if dsc_count == n - 1:
            left_rot = n - nums[-1] + 1
            right_rot = (nums[0] + 1) % n + 1
            return min(left_rot, right_rot)
            
        return -1