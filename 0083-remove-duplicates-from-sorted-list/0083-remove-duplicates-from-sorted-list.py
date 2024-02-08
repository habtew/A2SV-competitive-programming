# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head

        while current.next is not None:
            if current.val == current.next.val:
                # Duplicate found, update the next pointer to skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head