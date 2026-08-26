class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        min_len = n + 1
        
        count = 0
        left = 0
        
        for right in range(n):
            if s[right] == '1':
                count += 1

            while count == k:

                while s[left] == '0':
                    left += 1
                
                curr_sub = s[left : right + 1]
                curr_len = len(curr_sub)
                
             
                if curr_len < min_len:
                    min_len = curr_len
                    ans = curr_sub
                elif curr_len == min_len:
                    ans = min(ans, curr_sub)

                if s[left] == '1':
                    count -= 1
                left += 1
                
        return ans