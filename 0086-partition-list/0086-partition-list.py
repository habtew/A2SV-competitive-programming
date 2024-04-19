# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = left_tail = ListNode()
        right_head = right_tail = ListNode()

        curr = head
        while curr:
            if curr.val < x:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next
            curr = curr.next
        
        left_tail.next = right_head.next
        right_tail.next = None

        return left_head.next