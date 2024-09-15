# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        q = deque([root])

        while q:
            # print(curr.val)
            arr = []
            for _ in range(len(q)):
                curr = q.popleft()
                arr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(arr)
        ans = []
        for arr in res:
            ans.append(sum(arr) / len(arr))
        return ans
