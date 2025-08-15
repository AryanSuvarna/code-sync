# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)

        # get to starting position first (left node)
        leftPrev = dummyNode # keeps track of whatever is on the left side of the reversed chunk
        curr = head
        for _ in range(left - 1):
            leftPrev, curr = curr, curr.next
        
        # now that we are on left, keep reversing all until we reach 'right' or end of the list
        prev = None
        for _ in range(right - left + 1):
            currNext = curr.next
            curr.next = prev
            prev, curr = curr, currNext
        
        # readjust left and right pointers of the reversed chunk.
        leftPrev.next.next = curr # leftPrev.next is the end of the reversed
        leftPrev.next = prev #prev holds the head of the reversed
        

        return dummyNode.next