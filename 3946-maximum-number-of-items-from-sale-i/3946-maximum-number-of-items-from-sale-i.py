class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n= len(items)

        free = [0]*n

        minPrice = min(x[1] for x in items)

        for i in range(n):
            for j in range(n):
                
                if i != j and items[j][0] % items[i][0] ==0:
                    free[i] += 1

        dp = [0] * (budget +1)

        for i in range(n):
            price = items[i][1]

            for j in range(budget,price - 1 , -1):
                dp[j] = max(dp[j] , dp[j-price] + free[i] +1)

        ans = 0

        for j in range(budget +1):
            ans = max(ans,dp[j] + (budget-j) // minPrice)

        return ans
   