# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)

        dfs(root)
        new_root = TreeNode(nums[0])
        head = new_root
        for i in range(1, len(nums)):
            new_t = TreeNode(nums[i])
            head.right = new_t
            head.left = None
            head = new_t
        

        return new_root