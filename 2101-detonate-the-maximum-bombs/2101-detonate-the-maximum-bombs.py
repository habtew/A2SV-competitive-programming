class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def in_detonation_range(i, j):
            return (bombs[i][2] ** 2) >= ((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2)
        
        def dfs(bomb_index, visited):
            visited.add(bomb_index)
            count = 1
            for adjacent in detonation_graph[bomb_index]:
                if adjacent not in visited:
                    count += dfs(adjacent, visited)
            return count
        
        detonation_graph = defaultdict(list)
        num_bombs = len(bombs)
        
        for i in range(num_bombs):
            for j in range(num_bombs):
                if i != j and in_detonation_range(i, j):
                    detonation_graph[i].append(j)

        max_detonations = 0
        
        for bomb_index in range(num_bombs):
            visited = set()
            max_detonations = max(max_detonations, dfs(bomb_index, visited))
        
        return max_detonations