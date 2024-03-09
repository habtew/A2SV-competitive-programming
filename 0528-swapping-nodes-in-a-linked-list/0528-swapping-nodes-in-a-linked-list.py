# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        nums[k - 1], nums[len(nums) - k] = nums[len(nums) - k], nums[k - 1]
        current = ListNode(nums[0])
        head = current
        for val in nums[1:]:
            current.next = ListNode(val)
            current = current.next
        return head