class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)      
        indegrees = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
      
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        count = 0
      
        while queue:
            course = queue.popleft()
            count += 1
    
            for successor in graph[course]:
                indegrees[successor] -= 1
              
                if indegrees[successor] == 0:
                    queue.append(successor)
      
        return count == numCourses