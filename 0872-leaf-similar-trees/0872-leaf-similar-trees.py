# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        def dfs(root, arr):
            if not root:
                return arr
            if not root.left and not root.right:
                arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
            return arr
        leaf1 = dfs(root1, [])
        leaf2 = dfs(root2, [])

        return leaf1 == leaf2