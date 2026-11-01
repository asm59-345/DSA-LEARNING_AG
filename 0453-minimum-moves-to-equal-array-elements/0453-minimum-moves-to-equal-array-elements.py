class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        total_sum = sum(nums)
        return total_sum - len(nums) * min_val