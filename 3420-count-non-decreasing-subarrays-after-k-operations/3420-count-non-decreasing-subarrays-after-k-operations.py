from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        ans = 0
        operations = 0

        dq = deque()
        right = n - 1

        for left in range(n - 1, -1, -1):

            # Maintain decreasing deque
            while dq and nums[dq[-1]] < nums[left]:

                idx = dq.pop()
                prev = dq[-1] if dq else right + 1

                operations += (prev - idx) * (nums[left] - nums[idx])

            dq.append(left)

            # Shrink window if operations exceed k
            while operations > k:

                operations -= nums[dq[0]] - nums[right]

                if dq[0] == right:
                    dq.popleft()

                right -= 1

            # Count valid subarrays
            ans += right - left + 1

        return ans