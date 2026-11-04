from sortedcontainers import SortedList
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # 1. Precalculate costs for every window of size x
        lower = SortedList()
        upper = SortedList()
        sum_lower = 0
        sum_upper = 0
        
        def add(val):
            nonlocal sum_lower, sum_upper
            if not lower or val <= lower[-1]:
                lower.add(val)
                sum_lower += val
            else:
                upper.add(val)
                sum_upper += val
            balance()
            
        def remove(val):
            nonlocal sum_lower, sum_upper
            if val in lower:
                lower.remove(val)
                sum_lower -= val
            else:
                upper.remove(val)
                sum_upper -= val
            balance()
            
        def balance():
            nonlocal sum_lower, sum_upper
            while len(lower) > len(upper) + 1:
                val = lower.pop(-1)
                sum_lower -= val
                upper.add(val)
                sum_upper += val
            while len(lower) < len(upper):
                val = upper.pop(0)
                sum_upper -= val
                lower.add(val)
                sum_lower += val

        costs = [0] * (n - x + 1)
        
        for i in range(x):
            add(nums[i])
            
        for i in range(n - x + 1):
            if i > 0:
                remove(nums[i - 1])
                add(nums[i + x - 1])
            
            median = lower[-1]
            cost = (median * len(lower) - sum_lower) + (sum_upper - median * len(upper))
            costs[i] = cost

        # 2. Dynamic Programming

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        
        for i in range(n + 1):
            dp[0][i] = 0
            
        for j in range(1, k + 1):
            for i in range(1, n + 1):
                dp[j][i] = dp[j][i - 1]
                start_idx = i - x
                if start_idx >= 0:
                    prev_cost = dp[j - 1][start_idx]
                    if prev_cost != INF:
                        dp[j][i] = min(dp[j][i], prev_cost + costs[start_idx])
                        
        return dp[k][n]