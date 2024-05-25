# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def inord(root, i, j):
            if root is None:
                return
            result.append((j, i, root.val))
            inord(root.left, i + 1, j - 1)
            inord(root.right, i + 1, j + 1)

        inord(root, 0, 0)
        result.sort()
        ans = []
        prev = -2000
        for j, _, val in result:
            if prev != j:
                ans.append([])
                prev = j
            ans[-1].append(val)
        return ans