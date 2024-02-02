class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for c in logs:
            if not stack and c == '../':
                continue
            elif stack and c == '../':
                stack.pop()
            elif c == './':
                continue
            else:
                stack.append(c)
        return len(stack)