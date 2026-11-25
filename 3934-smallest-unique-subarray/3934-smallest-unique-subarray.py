from collections import Counter
from typing import List

class Solution:

  def smallestUniqueSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
      return n

    b1, m1 = 100003, (1 << 61) - 1
    b2, m2 = 100019, 10**9 + 9

    p1 = [1] * (n + 1)
    p2 = [1] * (n + 1)
    for i in range(1, n + 1):
      p1[i] = (p1[i - 1] * b1) % m1
      p2[i] = (p2[i - 1] * b2) % m2

    def has_unique(k: int) -> bool:
      if k == n:
        return True

      h1 = h2 = 0
      for i in range(k):
        h1 = (h1 * b1 + nums[i]) % m1
        h2 = (h2 * b2 + nums[i]) % m2

      counts = Counter([(h1, h2)])
      top1, top2 = p1[k - 1], p2[k - 1]

      for i in range(k, n):
        left = nums[i - k]
        h1 = ((h1 - left * top1) * b1 + nums[i]) % m1
        h2 = ((h2 - left * top2) * b2 + nums[i]) % m2
        counts[(h1, h2)] += 1

      return any(c == 1 for c in counts.values())

    lo, hi = 1, n
    while lo < hi:
      mid = (lo + hi) // 2
      if has_unique(mid):
        hi = mid
      else:
        lo = mid + 1

    return lo