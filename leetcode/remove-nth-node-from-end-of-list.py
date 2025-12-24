# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ONE PASS METHOD
        
        dummy = ListNode(0, head)
        fast = slow = dummy

        # move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # now we update slow ptr till the fast ptr reaches the end of the list
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # once we reach end of list, the slow ptr is one node away from node to be removed
        slow.next = slow.next.next

        return dummy.next