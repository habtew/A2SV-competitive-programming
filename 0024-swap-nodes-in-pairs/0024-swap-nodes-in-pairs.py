# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        i = 0
        while i < len(nums) - 1:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        current = ListNode(nums[0])
        head= current
        for val in nums[1:]:
            current.next = ListNode(val)
            current = current.next
        return head