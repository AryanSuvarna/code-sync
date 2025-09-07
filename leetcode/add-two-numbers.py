# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add the numbers together and create a new LL
        first_num, second_num = l1, l2
        sum_LL = ListNode()
        head = sum_LL

        carry = 0
        while first_num or second_num or carry:
            # get the values if the pointers aren't None, otherwise set to 0
            first_val = first_num.val if first_num else 0
            second_val = second_num.val if second_num else 0

            calc = first_val + second_val + carry

            # get carry value if calc is greater than 10
            carry = 1 if calc >= 10 else 0

            # take the remainder as the new node value
            head.next = ListNode(calc % 10, None)

            # update the pointers
            head = head.next
            # edge case: we have carry but no first and second values
            first_num = first_num.next if first_num else None
            second_num = second_num.next if second_num else None
            
        return sum_LL.next