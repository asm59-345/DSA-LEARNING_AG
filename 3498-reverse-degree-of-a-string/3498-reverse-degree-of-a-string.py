class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            pos_in_string = i + 1
            rev_alphabet = 26 - (ord(char) - ord('a'))
            total += rev_alphabet * pos_in_string

        return total 