# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # L1: 0 -> 1 -> 3 -> 5 -> 8 -> 10
        # L2: 1 -> 2 -> 4 -> 6
        # Final: 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 8 -> 10
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # dummyHead = tail = ListNode()
        # l1, l2 = list1, list2

        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next

        #     tail = tail.next
        
        # tail.next = l1 or l2
        # return dummyHead.next
