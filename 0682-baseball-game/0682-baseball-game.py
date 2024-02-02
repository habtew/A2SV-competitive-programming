class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if stack and c == 'C':
                stack.pop()
            elif stack and c == 'D':
                stack.append(2 * stack[-1])
            elif c == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(c))
        
        return sum(stack)