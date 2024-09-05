class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()
        
        sami = ans = sum(beans)
        n = len(beans)
        
        for i, val in enumerate(beans):
            ans = min(ans, sami - val * (n - i))

        return ans