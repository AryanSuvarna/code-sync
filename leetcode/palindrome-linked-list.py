# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # find the middle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of LL
        curr = slow
        prev = None
        while curr:
            currNxt = curr.next
            curr.next = prev
            prev = curr
            curr = currNxt    

        # compare each value of the list
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            if secondHalf.val != firstHalf.val:
                return False
            secondHalf = secondHalf.next
            firstHalf = firstHalf.next
        
        return True