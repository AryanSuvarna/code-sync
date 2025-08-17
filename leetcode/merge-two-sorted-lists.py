# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        # base cases
        if not list1:
            return list2
        if not list2:
            return list1

        # check both lists until one list gets empty
        l1Ptr, l2Ptr = list1, list2
        curr = dummyNode

        while l1Ptr and l2Ptr:
            if l1Ptr.val < l2Ptr.val:
                curr.next = l1Ptr
                l1Ptr = l1Ptr.next
                curr = curr.next
            else:
                curr.next = l2Ptr
                l2Ptr = l2Ptr.next
                curr = curr.next
        
        curr.next = l1Ptr or l2Ptr

        return dummyNode.next