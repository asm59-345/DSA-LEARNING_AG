class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        
        if sum(diff) <= total_k:
            return 0
            
        max_diff = max(diff)
        count = [0] * (max_diff + 1)
        for d in diff:
            count[d] += 1
            
        current_diff = max_diff
        while total_k > 0 and current_diff > 0:
            if count[current_diff] == 0:
                current_diff -= 1
                continue
            
            take = min(total_k, count[current_diff])
            count[current_diff] -= take
            count[current_diff - 1] += take
            total_k -= take
            current_diff -= 1
            
        ans = 0
        for d in range(max_diff + 1):
            if count[d] > 0:
                ans += count[d] * (d ** 2)
        return ans