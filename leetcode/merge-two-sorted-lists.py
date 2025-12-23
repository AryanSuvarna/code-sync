# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode()
        
        # base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        curr_1, curr_2 = list1, list2

        curr = dummy_node

        # if both pointers have something, we need to determine which one to append
        while curr_1 and curr_2:
            if curr_1.val < curr_2.val:
                curr.next = curr_1
                curr_1 = curr_1.next
                curr = curr.next
            else:
                curr.next = curr_2
                curr_2 = curr_2.next
                curr = curr.next
        
        # we exited while loop (one or both 2 pointers are empty). if there is still nodes remaining, just append to curr.next
        if curr_1:
            curr.next = curr_1
        elif curr_2:
            curr.next = curr_2
        
        return dummy_node.next