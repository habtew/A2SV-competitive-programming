class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(index, curr):
            if len(curr) == k and sum(curr) == n and curr not in res:
                res.append(curr.copy())
            for i in range(index, 10):
                curr.append(i)
                dfs(i + 1, curr)
                curr.pop()

        dfs(1, [])
        return res
