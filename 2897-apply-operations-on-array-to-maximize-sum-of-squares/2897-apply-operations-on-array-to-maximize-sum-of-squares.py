class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        
        for num in nums:
            for i in range(30):

                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        max_nums = [0] * k
        
        for i in range(30):
            count = bit_counts[i]

            for j in range(min(count, k)):
                max_nums[j] |= (1 << i)
                
        ans = 0
        for num in max_nums:
            ans = (ans + num * num) % MOD
            
        return ans