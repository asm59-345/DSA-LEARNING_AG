class Solution:
    def minOperations(self, s: str) -> int:

        if list(s) == sorted(s): # if list(s) == sorted(s):
            return 0             # return 0

        if len(s) == 2:           # if len(s) == 2:
            return -1             # return -1

        smallest = min(s)         #smallest = min(s)
        largest = max(s)          # largest = max(s)

        if len(set(s)) > 1:                       
            if s[0] == smallest or s[-1] == largest:
                return 1

        if s.count(smallest) == 1 and s[-1] == smallest:
            if s.count(largest) == 1 and s[0] == largest:
                return 3

        
        return 2