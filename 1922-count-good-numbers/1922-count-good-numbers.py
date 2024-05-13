class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, n):
            if n == 0:
                return 1
            res = power(x, n // 2)
            res = (res * res) % mod
            if n % 2:
                res = (res * x) % mod
            return res

        mod = 10**9 + 7
        even_pos = n // 2
        odd_pos = (n + 1) // 2

        count_even = power(4, even_pos) % mod
        count_odd = power(5, odd_pos) % mod

        return (count_even * count_odd) % mod
