# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def map_parents(node, parent):
            if node:
                parent_map[node] = parent
                map_parents(node.left, node)
                map_parents(node.right, node)

        def find_dk(node, rem):
            if not node or node.val in visited:
                return
            visited.add(node.val)
            if rem == 0:
                res.append(node.val)
            else:
                find_dk(node.left, rem - 1)
                find_dk(node.right, rem - 1)
                find_dk(parent_map[node], rem - 1)

        parent_map = {}
        res = []
        visited = set()

        map_parents(root, None)
        find_dk(target, k)
    
        return res