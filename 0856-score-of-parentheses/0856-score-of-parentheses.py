class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack =[0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                val = stack.pop()
                if val > 0:
                    val *= 2
                else:
                    val = 1
                stack.append(val + stack.pop())
        return stack[0]