class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        
        for c1, c2 in zip(s, t):
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False
            elif c2 in mapping.values():  
                return False
            else:
                mapping[c1] = c2
                
        return True