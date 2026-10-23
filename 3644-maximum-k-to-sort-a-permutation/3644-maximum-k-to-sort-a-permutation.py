class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i in range(len(nums)):
            if nums[i] != i:
                if k == -1:
                    k = nums[i]
                else:
                    k &= nums[i]
        return 0 if k ==-1 else k
'''
        k = -1
        for i , val in enumerate(nums):
            if val != i:
                k &= ( i & val)
        return 0 if k == -1 else k 
'''