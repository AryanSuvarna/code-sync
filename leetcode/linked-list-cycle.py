# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # base cases
        if not head:
            return False
        if head and head.next == None:
            return False
        
        slow = head
        fast = head.next

        while fast and fast.next:
            # ever come back to same node, we have dupe
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False