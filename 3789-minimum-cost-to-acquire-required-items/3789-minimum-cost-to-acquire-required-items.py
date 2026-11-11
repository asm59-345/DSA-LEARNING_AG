class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1 , need2)
        total_cost = common * min(costBoth, cost1 + cost2)

        if need1 > need2:
            rem1 = need1-need2
            total_cost += rem1 * min(costBoth, cost1)

        elif need2 > need1:
            rem2 = need2 - need1 
            total_cost += rem2 * min(costBoth, cost2)
            
        return total_cost
