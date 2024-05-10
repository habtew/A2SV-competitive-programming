class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        n = len(citations)

        while left <= right:
            mid = (left + right) // 2
            h = n - mid
            if citations[mid] == h:
                return citations[mid]
            elif citations[mid] > h:
                right = mid - 1
            else:
                left = mid + 1
        
        return n - left