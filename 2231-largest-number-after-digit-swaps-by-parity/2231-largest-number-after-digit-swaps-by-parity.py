class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(d) for d in str(num)]

        even = [d for d in digits if d % 2 == 0]
        odd = [d for d in digits if d % 2 != 0]
        even.sort(reverse=True)
        odd.sort(reverse=True)

        result = []
        for d in digits:
            if d % 2 == 0:
                result.append(even.pop(0))
            else:
                result.append(odd.pop(0))

        result_num = int(''.join(map(str, result)))
        return result_num
