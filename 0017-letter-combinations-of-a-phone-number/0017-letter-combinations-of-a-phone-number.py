class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(index: int, current_str: str):
            
            if index == len(digits):
                result.append(current_str)
                return
                
            for char in phone_map[digits[index]]:
                backtrack(index + 1, current_str + char)

        backtrack(0, "")
        return result