# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle point of the linked list
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of LL
        prev, curr = None, slow.next

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev, curr = curr, curr_next

        # compare
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True