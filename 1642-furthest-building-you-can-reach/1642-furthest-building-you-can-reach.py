import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        diff_heap = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heapq.heappush(diff_heap, diff)
                
                if len(diff_heap) > ladders:
                    bricks -= heapq.heappop(diff_heap)
                    
                    if bricks < 0:
                        return i
        
        return n - 1
        