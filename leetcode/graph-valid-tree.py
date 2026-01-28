class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # ARYAN

        # valid tree:
        #   1. no loops
        #   2. all nodes must be connected

        # create adjacency list
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        # visited set will keep count of the nodes that we visit
        visited = set()

        def dfs(curr, prev):
            # cycle detected
            if curr in visited:
                return False
            
            # dfs ....
            visited.add(curr)
            # go thru every neighboutr
            for neighbour in adj_list[curr]:
                # make sure neighbour is not previous value
                # then make sure that the dfs of neighbour doesnt return False
                if neighbour != prev and not dfs(neighbour, curr):
                    return False
            
            # return true if we successfully looked at all neighbours
            return True
        
        # run dfs on node 0 (prev value initially will be -1 as all node values are positive)
        if not dfs(0, -1): return False

        # if length of visited set is same as n, indicates that all nodes are connected
        return True if len(visited) == n else False