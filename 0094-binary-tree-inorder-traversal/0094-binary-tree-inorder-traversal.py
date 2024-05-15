# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inord(root):
            if root is None:
                return
            inord(root.left)
            ans.append(root.val)
            inord(root.right)
        inord(root)
        return ans