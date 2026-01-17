"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # hashmap to keep track of the new copied nodes
        old_to_new = {}

        # we will run dfs on each node to construct its neighbours
        def dfs(node):
            # node copy already exists in hashmap
            if node in old_to_new:
                return old_to_new[node]
            
            # make a copy of node and store in hashmap
            node_copy = Node(node.val)
            old_to_new[node] = node_copy

            # iterate on the neighbors of node
            for neighbor in node.neighbors:
                node_copy.neighbors.append(dfs(neighbor))
            
            return node_copy
        
        return dfs(node)