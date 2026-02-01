class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent_roots = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            # n is the root parent
            if n == parent_roots[n]:
                return n

            # recursively call find on the root
            parent_roots[n] = find(parent_roots[n])

            return parent_roots[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            # same parent! return early
            if p1 == p2: return False

            if rank[p1] > rank[p2]:
                parent_roots[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent_roots[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for n1, n2, in edges:
            if not union(n1, n2):
                return [n1, n2]