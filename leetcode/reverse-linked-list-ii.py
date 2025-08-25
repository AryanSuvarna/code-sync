# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # set up dummy_node
        dummy_node = ListNode(0, head)
        node_before_reversal = dummy_node

        # iterate thru LL until you come to left position
        left_pointer = head

        for _ in range(left - 1):
            left_pointer = left_pointer.next
            node_before_reversal = node_before_reversal.next

        # reverse right - left + 1 nodes
        prev, curr = None, left_pointer

        for _ in range(right - left + 1):
            curr_next = curr.next
            curr.next = prev
            prev, curr = curr, curr_next
        
        # rewire the nodes
        node_before_reversal.next.next = curr
        node_before_reversal.next = prev

        return dummy_node.next