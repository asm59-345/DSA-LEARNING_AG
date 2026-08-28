class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}

        for char in magazine:
            counts[char] = counts.get(char,0) +1

        for char in ransomNote:
            if counts.get(char,0) <= 0:
                return False
                
            counts[char] -= 1
        return True 
