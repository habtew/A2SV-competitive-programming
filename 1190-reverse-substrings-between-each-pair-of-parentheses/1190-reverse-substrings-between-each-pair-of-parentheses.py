class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
        return ''.join(stack)
        