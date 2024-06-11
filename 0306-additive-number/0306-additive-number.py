class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(first, second, remaining):
            while remaining:
                next_num = str(first + second)
                if not remaining.startswith(next_num):
                    return False
                remaining = remaining[len(next_num):]
                first, second = second, int(next_num)
            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                if (first.startswith("0") and first != "0") or (second.startswith("0") and second != "0"):
                    continue
                if valid(int(first), int(second), num[j:]):
                    return True

        return False