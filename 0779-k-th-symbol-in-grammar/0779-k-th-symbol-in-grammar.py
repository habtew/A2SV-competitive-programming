class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(level, index, answer):
            if level == 1:
                return answer
            if index % 2 == 1:
                return rec(level - 1, (index + 1) // 2, answer)
            return rec(level - 1, (index) // 2, 1 - answer)
        symbol = rec(n, k, 0)
        if symbol == 0:
            return 0
        return 1