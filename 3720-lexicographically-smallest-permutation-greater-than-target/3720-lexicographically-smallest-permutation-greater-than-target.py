from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq= Counter(s)
      
        for i in range(n - 1, -1, -1):
            prefix_freq = Counter(target[:i])

            if any(prefix_freq[ch] > freq[ch] for ch in prefix_freq):
                continue
            rem_freq = freq - prefix_freq

            for c in sorted(rem_freq.keys()):
                if c> target[i] and rem_freq[c] > 0:
                    rem_freq[c] -= 1

                    tail = "".join(ch * rem_freq[ch] for ch in sorted(rem_freq.keys()))
                    return target[:i] + c + tail
        return ""