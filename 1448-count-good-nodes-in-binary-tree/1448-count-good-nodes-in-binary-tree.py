# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if not node:
                return 0
            
            total = 0
            if node.val >= curr_max:
                total += 1
            total += dfs(node.left, max(node.val, curr_max))
            total += dfs(node.right, max(node.val, curr_max))
            
            return total
        return dfs(root, float('-inf'))