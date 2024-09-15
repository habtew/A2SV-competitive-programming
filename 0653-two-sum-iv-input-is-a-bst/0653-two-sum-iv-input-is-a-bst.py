# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        nums = []
        dfs(root)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            if nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1

        return False