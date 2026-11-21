class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]

        for i in range(1,n):
            adj[parent[i]].append(i)

        new_parent = parent[:]

        last = {}

        def dfs(u):
            ch = s[u]

            if ch in last:
                new_parent[u] = last[ch]

            old = last.get(ch)
            last[ch] = u

            for v in adj[u]:
                dfs(v)
            if old is None:
                del last[ch]
            else:
                last[ch] = old
        dfs(0)

        tree = [[] for _ in range(n)]

        for i in range(1,n):
            tree[new_parent[i]].append(i)

        ans = [0]*n


        def calculate(u):
            ans[u] = 1

            for v in tree[u]:
                ans[u] += calculate(v)
            return ans[u]
        calculate(0)

        return ans

