class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        new_s = ''
        for c in s:
            if c != '-':
                new_s += c.upper()
                count += 1
        res = []
        rem = count % k
        if rem != 0:
            res.append(new_s[:rem])
        for i in range(rem, len(new_s), k):
            res.append(new_s[i:i + k])
        print(res)
        return '-'.join(res)