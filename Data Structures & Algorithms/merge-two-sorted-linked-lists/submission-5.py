# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = dummytail = ListNode()
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                dummytail.next = l1
                l1 = l1.next
            else:
                dummytail.next = l2
                l2 = l2.next
            dummytail = dummytail.next

        if l1:
            dummytail.next = l1
        if l2:
            dummytail.next = l2
        
        return dummyhead.next
