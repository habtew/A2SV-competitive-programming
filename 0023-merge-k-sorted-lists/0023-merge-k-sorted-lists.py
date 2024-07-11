# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for nums in lists:
            current = nums
            while current:
                result.append(current.val)
                current = current.next

        if not result:
            return None
        result.sort()
        current = ListNode(result[0])
        head = current
        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next
        return head