import bisect
import functools
import math
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Sort intervals by (left, right, weight, original_index)
        sorted_intervals = sorted((*interval, i) for i, interval in enumerate(intervals))
        n = len(sorted_intervals)

        @functools.lru_cache(None)
        def dp(i: int, quota: int):
            # Base case: reached end of list or quota exhausted
            if i == n or quota == 0:
                return (0, ())

            # Option 1: Skip current interval
            skip_weight, skip_indices = dp(i + 1, quota)

            # Option 2: Pick current interval
            l, r, weight, orig_idx = sorted_intervals[i]
            
            # Binary search for the next interval starting after `r`
            j = bisect.bisect_right(sorted_intervals, (r, math.inf))
            
            next_weight, next_indices = dp(j, quota - 1)
            
            # Combine current weight and current index with remaining selection
            pick_weight = weight + next_weight
            pick_indices = tuple(sorted((orig_idx, *next_indices)))

            # Tie-breaking for maximum weight and lexicographically smallest indices
            if pick_weight > skip_weight:
                return (pick_weight, pick_indices)
            elif pick_weight < skip_weight:
                return (skip_weight, skip_indices)
            else:
                # If weights are equal, choose lexicographically smaller tuple
                return (pick_weight, min(pick_indices, skip_indices))

        return list(dp(0, 4)[1])