# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # S: 0 -> 1 -> 2 -> 3 -> 4 ->> 
        # I: 4 -> 3 -> 2 -> 1 -> 0 ->>
        # E: 4 -> 3 -> 2 -> 1 -> 0 ->>
        if head is None or head.next is None:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head # This creates the reverse link
        head.next = None  # This is removes the previous link
        return newHead
