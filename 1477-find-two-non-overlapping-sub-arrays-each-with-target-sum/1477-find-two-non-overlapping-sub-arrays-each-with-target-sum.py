class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        ans = float('inf')
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == target:
                curr_len = right - left + 1
                
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                prev_min = min_len[right - 1] if right > 0 else float('inf')
                min_len[right] = min(prev_min, curr_len)
            else:
                if right > 0:
                    min_len[right] =  min_len[right - 1]
                    
        return ans if ans != float('inf') else -1