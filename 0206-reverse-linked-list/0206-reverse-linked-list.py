# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(state):
            # base case
            if not state or not state.next:
                return state, state
            
            # recur
            tail, head_unc = rec(state.next)
            tail.next = state
            state.next = None
            return state, head_unc
        tail, cur_head = rec(head)
        return cur_head


