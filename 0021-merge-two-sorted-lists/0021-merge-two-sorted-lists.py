# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []
        curr1 = list1
        # creating list from linked list
        while curr1:
            nums1.append(curr1.val)
            curr1 = curr1.next
        curr2 = list2
        while curr2:
            nums2.append(curr2.val)
            curr2 = curr2.next

        # merging two sorted lists
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        result.extend(nums1[i:])
        result.extend(nums2[j:])

        # convert list to linked list
        if not result:
            return None

        current = ListNode(result[0])
        head = current
        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next

        return head