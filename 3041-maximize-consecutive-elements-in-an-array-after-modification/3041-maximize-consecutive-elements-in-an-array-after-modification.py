'''class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
         8574113543
         9026340469
         8299835809  
        '''

from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        nums.sort()

        dp0 = 1
        dp1 = 1
        ans = 1

        for i in range(1,len(nums)):
            prev = nums[i -1]
            curr = nums[i]

            if curr == prev:
                dp1 = dp0 + 1

            elif curr == prev + 1:
                dp0 += 1
                dp1 += 1
            elif curr == prev + 2:
                dp0 = dp1 + 1
                dp1 = 1 
            else:
                dp0 = 1
                dp1 = 1
            ans = max(ans , dp0, dp1)
        return ans  
