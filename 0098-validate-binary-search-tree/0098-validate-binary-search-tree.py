# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # time complexity: o(n)
        # space complexity: o(n)
        def valide(head, min, max):
            if not head:
                return True
            if head.val <= min or head.val >= max:
                return False
            left = valide(head.left, min, head.val)
            right = valide(head.right, head.val, max)
            return left and right

        return valide(root, float('-inf'), float('inf'))