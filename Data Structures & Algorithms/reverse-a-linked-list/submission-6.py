# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev, curr = None, head
        while curr:
            nxt = curr.next  # keeping track of the remaining list
            curr.next = prev  # reverse the links
            # Move the prev, curr pointers ahead
            prev = curr
            curr = nxt
        
        return prev



            