from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len   = len(words[0])
        num_words  = len(words)
        total_len  = word_len * num_words
        word_count = Counter(words)
        result     = []
        
        for i in range(word_len):
            left = i
            right = i
            seen = Counter()
            count = 0
            
            while right + word_len <= len(s):
                w = s[right : right + word_len]
                right += word_len
                
                if w in word_count:
                    seen[w] += 1
                    count += 1

                    while seen[w] > word_count[w]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    if count == num_words:
                        result.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right
                    
        return result