class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        candi = []

        for i in range(n):
            for j in range(i+1, n+1):
                sub = s[i:j]
                if sub.count('1') == k:
                    candi.append(sub)
                    
        if not candi:
            return ""
        candi.sort(key = lambda x: (len(x),x))
        return candi[0]