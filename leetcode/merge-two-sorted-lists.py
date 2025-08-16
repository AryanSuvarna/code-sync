# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)

        if not list1:
            return list2
        if not list2:
            return list1
        
        l1Ptr = list1
        l2Ptr = list2
        
        mergedList = head

        while l1Ptr and l2Ptr:
            if l1Ptr.val < l2Ptr.val:
                mergedList.next = l1Ptr
                mergedList = mergedList.next
                l1Ptr = l1Ptr.next
            else:
                mergedList.next = l2Ptr
                mergedList = mergedList.next
                l2Ptr = l2Ptr.next

        if not l1Ptr:
            mergedList.next = l2Ptr
        elif not l2Ptr:
            mergedList.next = l1Ptr
        
        return head.next