class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [defaultdict(list) for _ in range(2)]
        for start, end in redEdges:
            graph[0][start].append(end)
        for start, end in blueEdges:
            graph[1][start].append(end)

        distances = [-1] * n
        visited = set()
        
        queue = deque([(0, 0), (0, 1)])
        distance = 0

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                if distances[node] == -1:
                    distances[node] = distance
                visited.add((node, color))
                
                next_color = 1 - color
                for neighbor in graph[next_color][node]:
                    if (neighbor, next_color) not in visited:
                        queue.append((neighbor, next_color))
            distance += 1
        
        return distances