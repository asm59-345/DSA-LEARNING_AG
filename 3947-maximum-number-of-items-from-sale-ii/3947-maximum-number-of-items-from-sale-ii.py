from collections import Counter

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        min_price = min(price for factor, price in items)
        max_factor = max(factor for factor, price in items)

        freq = Counter(factor for factor, price in items)

        count = [0] * (max_factor + 1)

        for f in range(1, max_factor + 1):
            count[f] = freq[f] - 1

            for j in range(2 * f, max_factor + 1, f):
                count[f] += freq[j]

        bonus = {}

        for factor, price in items:
            if count[factor] > 0 and price <= 2 * min_price:
                bonus[price] = bonus.get(price, 0) + count[factor]

        ans = 0

        for price in sorted(bonus):
            take = min(bonus[price], budget // price)

            ans += take * 2
            budget -= take * price

        ans += budget // min_price

        return ans