class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for key in rooms[curr]:
                dfs(key)

        visited = set()
        dfs(0)
        return len(visited) == len(rooms)
