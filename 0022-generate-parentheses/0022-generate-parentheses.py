class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, open_count, close_count):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_count < n:
                dfs(s + "(", open_count + 1, close_count)

            if close_count < open_count:
                dfs(s + ")", open_count, close_count + 1)

        dfs("", 0, 0)
        return res
        