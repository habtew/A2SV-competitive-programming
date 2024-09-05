class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sami = (len(rolls) + n) * mean - sum(rolls)
        
        
        if sami > n*6 or sami < n:
            return []
        
        res = [sami//n] * n
        for i in range(sami % n):
            res[i] += 1
        return res