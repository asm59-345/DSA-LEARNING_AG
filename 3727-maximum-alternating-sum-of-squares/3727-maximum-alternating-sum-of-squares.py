class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted ([x *x for x in nums])

        n= len(sq)
        mid = n//2

        sub_sum = sum (sq [:mid])
        added_sum =  sum (sq[mid:])

        return added_sum - sub_sum