class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        res = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        queue = deque([i for i in range(numCourses) if incoming[i] == 0])
        print(queue)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        return res if len(res) == numCourses else []