class Solution:
    def smallestNumber(self, num: int) -> int:
        pos = True
        if num == 0:
            return 0
        if num < 0:
            pos = False
            num *= -1
        num_copy = num
        res = []
        
        while num_copy:
            n = num_copy % 10
            res.append(n)
            num_copy //= 10
        if pos:
            res.sort()
            if res[0] == 0:
                for i in range(len(res)):
                    if res[i] != 0:
                        res[0], res[i] = res[i], res[0]
                        break
            digit = 0
            for num in res:
                digit = digit * 10 + num
            return digit
        res.sort(reverse=True)
        digit = 0
        for num in res:
            digit = digit * 10 + num
        return digit*-1