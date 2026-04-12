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

        dummyHead = ListNode()
        tailNode = dummyHead
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                tailNode.next = l1
                tailNode = l1
                l1 = l1.next
            else:
                tailNode.next = l2
                tailNode = l2
                l2 = l2.next
        
        if l1:
            tailNode.next = l1
        if l2:
            tailNode.next = l2

        return dummyHead.next
