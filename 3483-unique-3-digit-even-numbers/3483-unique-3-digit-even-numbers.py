from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        valid_numbers = set()
        
        for p in permutations(digits, 3):
        
            if p[0] != 0 and p[2] % 2 == 0:
                valid_numbers.add(p)
                
        return len(valid_numbers)