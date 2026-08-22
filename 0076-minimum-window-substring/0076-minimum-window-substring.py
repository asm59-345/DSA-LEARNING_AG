from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()

        left = 0
        count = 0
        ans = ""

        for right in range(len(s)):
            window[s[right]] += 1

            if window[s[right]] <= need[s[right]]:
                count += 1

            while count == len(t):
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                window[s[left]] -= 1

                if window[s[left]] < need[s[left]]:
                    count -= 1

                left += 1

        return ans