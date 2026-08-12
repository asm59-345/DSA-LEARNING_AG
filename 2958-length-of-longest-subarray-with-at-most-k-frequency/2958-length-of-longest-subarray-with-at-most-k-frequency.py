class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) +1

            while counts[nums[right]] > k :
                counts[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left +1)
        return ans