class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        curr_num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                curr_num = curr_num *10 + int(char)

            elif char =='+':
                result += sign * curr_num
                curr_num = 0
                sign = 1

            elif char =='-':
                result += sign * curr_num
                curr_num = 0
                sign = -1

            elif char =='(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                
            elif char == ')':
                result += sign * curr_num
                curr_num = 0
                result *= stack.pop()
                result += stack.pop()
                  
        result += sign * curr_num
        return result               
                
            