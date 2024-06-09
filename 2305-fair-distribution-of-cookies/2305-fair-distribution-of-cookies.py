class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        res = [0] * k
        self.answer = float('inf')

        def dfs(index):
            if index >= len(cookies):
                self.answer = min(self.answer, max(res))
                return
            for i in range(k):
                if res[i] + cookies[index] >= self.answer or (i and res[i] == res[i - 1]):
                    continue
                res[i] += cookies[index]
                dfs(index + 1)
                res[i] -= cookies[index]
        dfs(0)

        return self.answer