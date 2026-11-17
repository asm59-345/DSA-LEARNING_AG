from typing import List
from functools import lru_cache

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)
        INF = 10**9

        # Precompute divisors
        divisors = [[] for _ in range(n + 1)]

        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # Precompute cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):

                length = j - i + 1
                best = INF

                for d in divisors[length]:

                    changes = 0

                    for start in range(d):

                        left = start
                        right = length - d + start

                        while left < right:

                            if s[i + left] != s[i + right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # DP: minimum cost to divide suffix into parts
        @lru_cache(None)
        def dp(i, parts):

            if parts == 0:
                return 0 if i == n else INF

            if n - i < 2 * parts:
                return INF

            ans = INF

            # Current substring must have length >= 2
            max_end = n - 2 * (parts - 1) - 1

            for j in range(i + 1, max_end + 1):

                ans = min(
                    ans,
                    cost[i][j] + dp(j + 1, parts - 1)
                )

            return ans

        return dp(0, k)