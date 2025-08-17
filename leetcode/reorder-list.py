# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get second half of list
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of list
        prev, curr = None, slow.next

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev, curr = curr, curr_next

        # one by one, add the list values in (we're modifying 'head' in place)
        slow.next = None # this breaks the relationship up between left and right

        while prev: # right half of list is always going to be smaller than left (our bottleneck in loop)
            prev_next = prev.next
            head_next = head.next

            # point head's next to prev and then prev's next to head's stored next
            head.next = prev
            prev.next = head_next

            head, prev = head_next, prev_next