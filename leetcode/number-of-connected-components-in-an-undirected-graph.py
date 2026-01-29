class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # ARYAN
        
        # create adjacency lis
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        def dfs(curr):
            visited.add(curr)

            for nei in adj_list[curr]:
                if nei not in visited:
                    dfs(nei)
            
        
        num_components = 0
        for i in range(n):
            if i not in visited:
                num_components += 1
                dfs(i)
        
        return num_components