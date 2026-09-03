
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            result[" " .join(sorted(s))].append(s)

        return list(result.values())