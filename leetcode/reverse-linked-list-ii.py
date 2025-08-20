# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # get to left 
        dummy_node = ListNode(0, head)

        prev_ptr, left_ptr = dummy_node, head
        

        for _ in range(left - 1):
            prev_ptr = left_ptr
            left_ptr = left_ptr.next

        # reverse the nodes from position 'left' to position 'right'    
        prev = None
        curr = left_ptr
        for _ in range(right - left + 1):
            curr_nxt = curr.next
            curr.next = prev
            prev, curr = curr, curr_nxt
        
        # rewire the nodes
        tail = prev_ptr.next
        prev_ptr.next = prev
        tail.next = curr

        return dummy_node.next