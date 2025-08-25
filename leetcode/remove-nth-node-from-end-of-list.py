# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the count of nodes in LL
        node_count = 0
        count_pointer = head

        while count_pointer:
            node_count += 1
            count_pointer = count_pointer.next
        
        # figure out the node to remove
        node_to_remove = node_count - n

        # edge case
        if node_to_remove == 0:
            return head.next
        
        # go to node right before the node we want to remove
        curr = head
        for _ in range(node_to_remove - 1):
            curr = curr.next
        
        # remove the node by rewiring it to the next
        curr.next = curr.next.next

        return head