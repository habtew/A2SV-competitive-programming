class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        
        if expected == heights:
            return 0
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count