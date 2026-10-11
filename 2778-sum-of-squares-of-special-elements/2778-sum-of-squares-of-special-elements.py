class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(x ** 2 for i, x in enumerate(nums, 1) if n % i == 0)