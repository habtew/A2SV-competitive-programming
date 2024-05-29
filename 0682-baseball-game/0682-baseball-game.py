class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if stack and operations[i] == '+':
                stack.append(stack[-1] + stack[-2])
            elif stack and operations[i] == 'D':
                num = stack[-1]
                stack.append(2 * num)
            elif stack and operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))
        
        return sum(stack)