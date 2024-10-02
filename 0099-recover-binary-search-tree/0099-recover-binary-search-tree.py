# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            nums.append(root)
            dfs(root.right)

        dfs(root)
        sorted_nums = sorted(node.val for node in nums)
        for i in range(len(nums)):
            nums[i].val = sorted_nums[i]