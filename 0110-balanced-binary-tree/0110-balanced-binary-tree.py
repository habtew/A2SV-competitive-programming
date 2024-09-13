# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = [True]
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_node = dfs(node.right)

            if abs(left_height - right_node) > 1:
                isBalanced[0] = False
                return 0
            return 1 + max(left_height, right_node)
        dfs(root)
        return isBalanced[0]