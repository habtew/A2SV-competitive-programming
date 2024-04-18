# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        time complexity - O(n)
        space complexity - O(1)
        """
        if head == None:
            return None
        
        curr = head
        count = 1
        while curr.next:
            count += 1
            curr = curr.next
        
        # make circular
        curr.next = head

        temp = head
        k %= count
        for i in range(count - k - 1 ):
            temp = temp.next
        
        new_head = temp.next
        temp.next = None

        return new_head