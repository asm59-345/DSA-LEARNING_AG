class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(char) - 97)) * (i + 1) for i, char in enumerate(s))