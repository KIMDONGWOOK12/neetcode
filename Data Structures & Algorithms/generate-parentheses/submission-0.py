class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, ing):
            if len(ing) == 2 * n:
                res.append(ing)
                return

            if open < n :
                dfs(open + 1, close, ing+ "(")
            if close < open :
                dfs(open, close + 1, ing + ")")

        dfs(0,0, "")
        return res