"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # adding edge case. if we are looking for copy of 'None', it should return 'None' as well
        old_to_new_map = {None: None}

        # first pass: just create the nodes and store relationship of old and new nodes
        curr = head

        while curr:
            new_node = Node(curr.val, None, None)
            old_to_new_map[curr] = new_node
            curr = curr.next
        
        # second pass: now create the links between the nodes (both the next and random pointers)
        old = head

        while old:
            new_node = old_to_new_map[old]

            # get the copied version of the 'next' node and 'random' node
            new_node.next = old_to_new_map[old.next]
            new_node.random = old_to_new_map[old.random]

            old = old.next
        
        # return the head copy
        return old_to_new_map[head]