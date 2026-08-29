class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        paired = sorted((val, idx) for idx, val in enumerate(nums))
        
        ans = [0] * n
        i = 0
        
        while i < n:
            j = i
            while j + 1 < n and paired[j + 1][0] - paired[j][0] <= limit:
                j += 1
            
            group_indices = sorted(paired[k][1] for k in range(i, j + 1))
            
            for k in range(i, j + 1):
                ans[group_indices[k - i]] = paired[k][0]
                
            i = j + 1
            
        return ans