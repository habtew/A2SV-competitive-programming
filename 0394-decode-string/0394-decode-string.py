class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                digit = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit) * word)
        return ''.join(stack)
        