class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')

        for comp in arr:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
                else:

                    continue

            else:
                stack.append(comp)
        
        return '/' + '/'.join(stack)