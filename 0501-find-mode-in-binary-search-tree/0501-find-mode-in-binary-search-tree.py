# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        def dfs(node):
            if not node:
                return
            if node.val in res:
                res[node.val] += 1
            else:
                res[node.val] = 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        maxi = max([num for num in res.values()])

        return [num for num, val in res.items() if val == maxi]