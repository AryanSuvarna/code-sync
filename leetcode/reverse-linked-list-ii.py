# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        
        # get to left position
        leftPtr = dummyNode
        curr = head
        for _ in range(left - 1):
            leftPtr = curr
            curr = curr.next

        # this is the left node that becomes the tail for the reversed sublist
        tail = curr

        # start reversing until reach right or end of list
        prev = None
        for _ in range(right - left + 1):
            currNxt = curr.next
            curr.next = prev
            prev = curr
            curr = currNxt

        # reconnect the elements together
        tail.next = curr
        leftPtr.next = prev

        return dummyNode.next