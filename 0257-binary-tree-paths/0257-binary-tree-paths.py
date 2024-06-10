# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, curr):
            if not node:
                return
            curr.append(str(node.val))
            # if leap node append current nodes to res
            if not node.left and not node.right:
                res.append('->'.join(curr))
            else:
                dfs(node.left, curr)
                dfs(node.right, curr)
            curr.pop()
        dfs(root, [])
        return res