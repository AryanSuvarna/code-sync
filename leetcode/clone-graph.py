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
        old_to_new = {}

        if not node:
            return

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]
            
            cloned = Node(curr.val)
            old_to_new[curr] = cloned           

            for n in curr.neighbors:
                cloned.neighbors.append(dfs(n))
            
            return cloned
        
        return dfs(node)