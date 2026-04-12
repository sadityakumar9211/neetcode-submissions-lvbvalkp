# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # I struggle at breaking the problem into smaller problems and 
        # finding solution to smaller problems is easy (otherwise I haven't broken to them small enough)
        # I also struggle to combine solutions of smaller problems into larger problem.
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev