# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # I can't visualize this 
        # Because I haven't visualized this in a long time, I don't have it in the memory
        # I need to increase familiarity with it. 
        # I need to solve it in paper. 
        # I tried doing code first, then doing dry run (aim in the dark.)
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev