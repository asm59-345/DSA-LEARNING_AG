class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair =[0] *n
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i 

        res = []
        curr = 0
        dir = 1

        while curr< n :
            if s[curr] in "()":
                curr = pair[curr]
                dir = - dir
            else:
                res.append(s[curr])
            curr += dir
        return "".join(res)