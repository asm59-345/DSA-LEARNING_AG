class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n , m = len(word1) , len(word2)

        suffix = [-1] * m 
        r = n-1

        for j in range(m - 1,-1,-1):
            while r >= 0 and word1[r] != word2[j]:
                r -= 1
            suffix[j] = r
            r -= 1
        res= []
        changed = False
        i = 0

        for j in range(m):
            while i < n:
                is_match = word1[i] == word2[j]
                can_finish = j + 1 == m or (i +1 < n and suffix[j+ 1] > i)

                if is_match or (not changed and can_finish):
                    if not is_match:
                        changed = True
                    res.append(i)
                    i+= 1 
                    break
                i += 1
        return res if len(res) == m else []