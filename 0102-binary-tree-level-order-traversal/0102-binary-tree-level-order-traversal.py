# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
      
        if root is None:
            return res
      
        queue = deque([root])
      
        while queue:
            level_values = []
          
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_values.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
            
                if curr.right:
                    queue.append(curr.right)
          
            res.append(level_values)
      
        return res