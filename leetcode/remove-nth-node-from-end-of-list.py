# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of LL
        count_ptr = head
        counter = 0

        while count_ptr:
            counter += 1
            count_ptr = count_ptr.next
        
        # determine node to remove
        node_to_remove = counter - n

        # remove this node
        
        if node_to_remove == 0:
            return head.next

        # go to node right before the node we want to remove
        curr = head
        for _ in range(node_to_remove - 1):
            curr = curr.next
        
        # remove the node by rewiring it to the next
        curr.next = curr.next.next

        return head