class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        used = [False] * n

        def dfs(curr):
            if len(curr) == n:
                if curr not in res:
                    res.append(curr.copy())
                    return
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()
                    used[i] = False
        dfs([])

        return res