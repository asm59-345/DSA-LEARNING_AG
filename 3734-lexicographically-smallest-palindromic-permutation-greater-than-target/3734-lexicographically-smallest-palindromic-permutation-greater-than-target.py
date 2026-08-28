from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        odd_char = ""
        odd_count = 0
        half_freq = Counter()
        
        for ch, count in freq.items():
            if count % 2 != 0:
                odd_count += 1
                odd_char = ch
            half_freq[ch] = count // 2
            
        if (n % 2 == 0 and odd_count != 0) or (n % 2 == 1 and odd_count != 1):
            return ""
            
        m = n // 2

        def make_pal(half: str) -> str:
            return half + odd_char + half[::-1]

        ans = None

        prefix_freq = Counter(target[:m])
        if all(half_freq[ch] >= prefix_freq[ch] for ch in prefix_freq):
            exact_half = target[:m]
            cand = make_pal(exact_half)
            if cand > target:
                ans = cand

        for i in range(m - 1, -1, -1):
            prefix_freq = Counter(target[:i])
            if any(half_freq[ch] < prefix_freq[ch] for ch in prefix_freq):
                continue
                
            rem_freq = half_freq - prefix_freq
 
            for c in sorted(rem_freq.keys()):
                if c > target[i] and rem_freq[c] > 0:
                    rem_freq[c] -= 1
        
                    tail = "".join(ch * rem_freq[ch] for ch in sorted(rem_freq.keys()))
                    half = target[:i] + c + tail
                    cand = make_pal(half)
                    
                    if ans is None or cand < ans:
                        ans = cand
                    break 

        return ans if ans is not None else ""