class Solution:
  def maxNumOfSubstrings(self, s: str) -> list[str]:
    first = {}
    last = {}
    for i, ch in enumerate(s):
      if ch not in first:
        first[ch] = i
      last[ch] = i

    intervals = []
    for ch in first:
      left, right = first[ch], last[ch]
      possible = True
      i = left
      while i <= right:
        if first[s[i]] < left:
          possible = False
          break
        right = max(right, last[s[i]])
        i += 1

      if possible:
        intervals.append((left, right))

    intervals.sort(key=lambda x: x[1])

    result = []
    prev_end = -1
    for left, right in intervals:
      if left > prev_end:
        result.append(s[left : right + 1])
        prev_end = right

    return result