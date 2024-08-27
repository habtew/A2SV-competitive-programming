class Solution:
    def countBits(self, n: int) -> List[int]:
        
        li = []
        def bitsIn(i):
            count = 0
            while i:
                if i % 2 == 1:
                    count += 1
                i //= 2
            return count
        for i in range(n + 1):
            li.append(bitsIn(i))
        return li