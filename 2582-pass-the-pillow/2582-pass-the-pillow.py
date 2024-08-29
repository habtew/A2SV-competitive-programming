class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # 1 -> 2 -> 3 -> 4 -> 3 -> 2 -> 1 -> 2 -> 3 -> 4 -> 3
        k = time // (n - 1)
        mode = time % (n - 1)
        if k & 1:
            return n - mode
        return mode + 1