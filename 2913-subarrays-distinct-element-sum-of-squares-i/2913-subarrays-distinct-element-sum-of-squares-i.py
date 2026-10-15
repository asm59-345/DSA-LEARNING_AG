class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        for i in range(n):
            for j in range(i,n):
                total_sum += len(set(nums[i:j+1])) ** 2
        return total_sum
