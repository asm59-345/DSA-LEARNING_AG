class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        
        sorted_nums = sorted([(val, idx) for idx, val in enumerate(nums)])
        
        result = [0] * n
        
        i = 0
        while i < n:
            j = i
            
            while j + 1 < n and sorted_nums[j + 1][0] - sorted_nums[j][0] <= limit:
                j += 1
            
            indices = sorted([sorted_nums[k][1] for k in range(i, j + 1)])
            
            for k in range(i, j + 1):
                val = sorted_nums[k][0]
                idx = indices[k - i]
                result[idx] = val
            
            i = j + 1
            
        return result