from collections import Counter
                                                     
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        left = 0
        count = 0
        min_len = float("inf")
        answer = ""

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] <= need[ch]:
                count += 1

            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    answer = s[left:right + 1]

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    count -= 1

                left += 1

        return answer