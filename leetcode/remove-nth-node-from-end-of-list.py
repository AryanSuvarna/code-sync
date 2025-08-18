# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # creating a dummy Node here is super helpful for dealing with edge cases
        dummy = ListNode(0, head)
        left, right = dummy, dummy
        
        # create a gap of n nodes between left and right pointers
        for _ in range(n + 1):
            right = right.next
        
        # iterate and update until right pointer reaches end of LL
        while right:
            left, right = left.next, right.next
        
        # the node we want to remove is the node right next to left ptr
        left.next = left.next.next
    
        return dummy.next