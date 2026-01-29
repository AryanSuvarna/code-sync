class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # ARYAN

        # create adjacency list
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)


        visited = set()
        
        # will return true/false
        def dfs(curr, prev):
            # cycle detected
            if curr in visited: return False

            visited.add(curr)
            # go thru every neighbour and run dfs
            for neighbour in adj_list[curr]:
                if neighbour != prev and not dfs(neighbour, curr):
                    return False
            
            # true if all neighbours are valid 
            return True
        
        if not dfs(0, -1): return False

        # only return True if we have visited all the nodes
        return True if len(visited) == n else False