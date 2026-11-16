class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)> k:
            new_groups = []
            
            for i in range(0, len(s), k):
                group = s[i:i + k]
                digit_sum = sum(int(char) for char in group)
                new_groups.append(str(digit_sum))
            s = "".join(new_groups)
        return s
