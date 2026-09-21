class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        prev_counts = [0] * k
        
        for num in nums:
            curr_counts = [0] * k
            val = num % k
            curr_counts[val] += 1
            
            for r in range(k):
                if prev_counts[r] > 0:
                    new_r = (r * val) % k
                    curr_counts[new_r] += prev_counts[r]
            
            for r in range(k):
                res[r] += curr_counts[r]
                
            prev_counts = curr_counts
            
        return res