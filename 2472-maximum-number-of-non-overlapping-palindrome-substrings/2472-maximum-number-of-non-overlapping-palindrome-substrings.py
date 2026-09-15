class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(n):
            dp[i+1] = max(dp[i], dp[i+1])
            
            self.update_dp(s, i, i, k, dp)
            self.update_dp(s, i, i+1, k, dp)
            
        return dp[n]

    def update_dp(self, s, l, r, k, dp):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 >= k:
                dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                break  
            l -= 1
            r += 1
            