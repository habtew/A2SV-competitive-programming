# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        nums = set()
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.add(node.val)
            
            dfs(node.right)
        dfs(root)
        nums = sorted(nums)
        print(nums)
        if len(nums) > 1:
            return nums[1]
        return -1