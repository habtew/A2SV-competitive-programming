# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        ans = float('-inf')
        while prev:
            ans = max(ans, prev.val + head.val)
            head = head.next
            prev = prev.next
        return ans