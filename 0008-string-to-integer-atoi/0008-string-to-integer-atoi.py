class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        digit = 0
        i = 0

        # Skip leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Check for sign
        if i < len(s) and s[i] == '-':
            sign *= -1
            i += 1
        elif i < len(s) and s[i] == '+':
            sign *= 1
            i += 1
        
        # Convert digits to integer
        while i < len(s) and s[i].isdigit():
            digit = digit * 10 + int(s[i])
            i += 1
        
        digit *= sign
        if digit <= -2147483648:
            digit = -2147483648
        elif digit >= 2147483647:
            digit = 2147483647
        
        return digit