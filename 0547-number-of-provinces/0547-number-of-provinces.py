class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(curr):
            visited[curr] = True
            for adj, connected in enumerate(isConnected[curr]):
                if not visited[adj] and connected:
                    dfs(adj)

        num_cities = len(isConnected)
        visited = [False] * num_cities
        count = 0
        for city in range(num_cities):
            if not visited[city]:
                dfs(city)
                count += 1

        return count