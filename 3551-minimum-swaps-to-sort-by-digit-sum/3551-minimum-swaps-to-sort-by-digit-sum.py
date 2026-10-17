from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
            
        n = len(nums)
        # Fixed 'num[i]' to 'nums[i]'
        arr = [(get_digit_sum(nums[i]), nums[i], i) for i in range(n)]

        sorted_arr = sorted(arr, key=lambda x: (x[0], x[1]))

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or sorted_arr[i][2] == i:
                continue
            
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = sorted_arr[curr][2]
                cycle_size += 1

            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps