# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        def dfs(node, curr_sum, curr):
            if not node:
                return
            curr.append(node.val)
            curr_sum += node.val

            if curr_sum == targetSum and (not node.left and not node.right):
                res.append(curr.copy())
            else:
                dfs(node.left, curr_sum, curr)
                dfs(node.right, curr_sum, curr)
            curr.pop()
        dfs(root, 0, [])
        
        return res != []