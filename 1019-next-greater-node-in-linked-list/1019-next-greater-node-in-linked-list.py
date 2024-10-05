# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
            
        n = len(values)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and values[i] > values[stack[-1]]:
                index = stack.pop()
                result[index] = values[i]
            stack.append(i)
        
        return result