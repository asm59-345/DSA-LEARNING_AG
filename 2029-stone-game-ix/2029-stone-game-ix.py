class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt =[0,0,0]
        for x in stones:
            cnt[x % 3] += 1
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]

        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        return abs(c1 - c2) >2