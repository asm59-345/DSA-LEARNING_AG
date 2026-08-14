class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = n - 1

        while i >= 0:
            # Skip trailing / intermediate spaces
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            
            end = i
            # Find the start of the current word
            while i >= 0 and s[i] != ' ':
                i -= 1
            
            # Extract word and add to result
            words.append(s[i + 1 : end + 1])

        return " ".join(words)