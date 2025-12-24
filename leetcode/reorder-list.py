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
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half starts on next node
        second_half = slow.next
        # make the first half end on None
        slow.next = None

        # reverse the second half
        prev = None

        while second_half:
            second_half_next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = second_half_next
        
        # now we combine both halves
        while prev:
            head_next, prev_next = head.next, prev.next

            head.next = prev
            prev.next = head_next

            prev = prev_next
            head = head_next
        
        return head