# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMid(head):
            prev = None
            slow = head
            fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow
        
        def reverse(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        def merge(l1, l2):
            while l2:
                temp = l1.next
                l1.next = l2
                l1 = l2
                l2 = temp
        if not head or not head.next:
            return
        mid = findMid(head)
        rever = reverse(mid)
        merge(head, rever)