class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for c in s:
            if stack_s and c == '#':
                stack_s.pop()
            elif not stack_s and c == '#':
                continue
            else:
                stack_s.append(c)
        for c in t:
            if stack_t and c == '#':
                stack_t.pop()
            elif not stack_t and c == '#':
                continue
            else:
                stack_t.append(c)
        return ''.join(stack_s) == ''.join(stack_t)
