# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        l1_ptr, l2_ptr = l1, l2
        carry = 0
        res = dummy
        
        while l1_ptr or l2_ptr or carry:
            first_val = l1_ptr.val if l1_ptr else 0
            second_val = l2_ptr.val if l2_ptr else 0

            calc = first_val + second_val + carry
            carry = 1 if calc >= 10 else 0

            res.next = ListNode(calc % 10, None)
            
            res = res.next
            l1_ptr = l1_ptr.next if l1_ptr else None
            l2_ptr = l2_ptr.next if l2_ptr else None
        
        return dummy.next