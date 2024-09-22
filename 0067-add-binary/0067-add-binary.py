class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1, n2 = len(a), len(b)
        ans = []
        if n1 > n2:
            b = '0'*(n1 - n2) + b
        else:
            a = '0'*(n2 - n1) + a

        carry = 0
        last = max(n1, n2) - 1
        for i in range(last, -1, -1):
            curr_sum = carry + int(a[i]) + int(b[i])
            if curr_sum == 3:
                ans.insert(0, '1')
                carry = 1
            elif curr_sum == 2:
                ans.insert(0, '0')
                carry = 1
            elif curr_sum == 1:
                ans.insert(0, '1')
                carry = 0
            else:
                ans.insert(0, '0')
                carry = 0
        if carry:
            return str(carry) + ''.join(ans)

        return ''.join(ans)