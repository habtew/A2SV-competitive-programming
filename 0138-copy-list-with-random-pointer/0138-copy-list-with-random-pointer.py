"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNewMap = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNewMap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToNewMap[curr]
            copy.next = oldToNewMap[curr.next]
            copy.random = oldToNewMap[curr.random]

            curr = curr.next


        return oldToNewMap[head]
        