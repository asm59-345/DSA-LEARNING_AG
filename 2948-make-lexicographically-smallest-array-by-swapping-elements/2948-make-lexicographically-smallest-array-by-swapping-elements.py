from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        sorted_nums = sorted(nums)
        
        groups = []        
        val_to_group = {}  
        
        for num in sorted_nums:
            if not groups or num - groups[-1][-1] > limit:
                groups.append(deque())
            
            groups[-1].append(num)
            val_to_group[num] = len(groups) - 1
            
        result = []
        for num in nums:
            group_idx = val_to_group[num]
            smallest_val = groups[group_idx].popleft()  
            result.append(smallest_val)
            
        return result