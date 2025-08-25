# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # base case (single node)
        if not head.next:
            return True
        
        # find middle of LL
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of LL
        curr, prev = slow.next, None

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev, curr = curr, curr_next
        
        # compare the reversed second half with the first half
        first, second = head, prev

        while second:
            if second.val != first.val:
                return False
            second = second.next
            first = first.next
        
        return True