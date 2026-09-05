class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suf_min = [0] *n
        suf_min[-1] = nums[-1]

        for i in range(n - 2, -1,-1):
            suf_min[i] = min(suf_min[i+1] , nums[i])

        pre_max = 0
        for i in range(n):
            pre_max = max(pre_max , nums[i])
            if pre_max - suf_min[i] <= k:
                return i
        return -1