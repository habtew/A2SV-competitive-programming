# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head
        curr = head
        len_ = 0
        while curr:
            len_ += 1
            curr = curr.next
        
        for i in range(k - 1):
            slow = slow.next
        
        for i in range(len_ - k):
            fast = fast.next
        
        tmp = slow.val
        slow.val = fast.val
        fast.val = tmp
        return head
