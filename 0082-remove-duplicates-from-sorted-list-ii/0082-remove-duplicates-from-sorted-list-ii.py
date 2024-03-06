# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next

        result = []
        left = 0
        while left < len(nums):
            if left == len(nums) - 1 or nums[left] != nums[left + 1]:
                result.append(nums[left])
            else:
                while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                    left += 1

            left += 1


        if not result:
            return None

        current = ListNode(result[0])
        head = current

        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next

        return head