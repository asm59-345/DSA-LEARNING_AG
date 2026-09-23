class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        
        n = len(nums)
        max_len =-1
        curr_sum = 0
        left = 0

        for right, val in enumerate(nums):
            curr_sum += val

            while curr_sum > target :           
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len , right- left + 1)
                
        return n - max_len if max_len != -1 else -1