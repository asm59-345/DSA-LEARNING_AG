class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_n = 0
        close_n = 0

        for ch in s:
            if ch== '(':
                close_n += 1
            else:
                if close_n >0:
                    close_n -= 1
                else:
                    open_n += 1
        return open_n + close_n