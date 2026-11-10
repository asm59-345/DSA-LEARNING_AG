class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):

            for k in range(1, 4):
                i = j - k
                if i >= 0:
                    jump_cost = costs[j - 1] + (j - i) ** 2
                    
                    dp[j] = min(dp[j], dp[i] + jump_cost)
                    
        return dp[n]