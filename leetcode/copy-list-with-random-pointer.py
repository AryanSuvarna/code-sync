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
        # first pass: create all the nodes and create mappings between old and new nodes
        old_to_new_map = {None: None}

        curr = head

        while curr:
            # just create nodes; connections will be added later
            new_node = Node(curr.val)
            old_to_new_map[curr] = new_node
            curr = curr.next
        
        # second pass: now we will add the connections for each node
        old_node = head

        while old_node:
            new_node = old_to_new_map[old_node]
            # add .next connections
            new_node.next = old_to_new_map[old_node.next]
            # add .random connections
            new_node.random = old_to_new_map[old_node.random]

            old_node = old_node.next
        
        # return the head of the new nodes
        return old_to_new_map[head]