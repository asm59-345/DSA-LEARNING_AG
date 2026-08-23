class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n//2

        sum_left = sum(int(c) for c in num [:half] if c != "?")
        sum_right = sum(int(c) for c in num [half:] if c != "?")

        q_left = num[:half].count("?")
        q_right = num[half:].count("?")

        if (q_left + q_right) % 2 !=0:
            return True
        
        diff_sum = sum_left - sum_right
        diff_q = q_right - q_left

        return diff_sum != (diff_q // 2) * 9
         