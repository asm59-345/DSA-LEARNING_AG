class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {0: [""]}
        
        def dp(k):
            if k in memo:
                return memo[k]
            
            ans = []
            for c in range(k):
                for left in dp(c):
                    for right in dp(k - 1 - c):
                        
                        ans.append(f"({left}){right}")
            
            memo[k] = ans
            return ans

        return dp(n)