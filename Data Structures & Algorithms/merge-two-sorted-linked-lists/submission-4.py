# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = dummyTail = ListNode()
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                dummyTail.next = l1
                l1 = l1.next
                dummyTail = dummyTail.next
            else:
                dummyTail.next = l2
                l2 = l2.next
                dummyTail = dummyTail.next
            
        if l1:
            dummyTail.next = l1
        
        if l2:
            dummyTail.next = l2
        
        return dummyHead.next
            
            




        