class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i+1, n +1):
                sub = s[i:j]
                if sub.count('1') == k:

                    if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                        ans = sub
        return ans