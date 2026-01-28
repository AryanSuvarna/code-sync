class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)

        for c, p in prerequisites:
            prereq_map[c].append(p)
        
        res = []
        visited, cycle = set(), set()
        
        def dfs(c):
            if c in cycle:
                return False
            
            if c in visited:
                return True

            cycle.add(c)
            for p in prereq_map[c]:
                if not dfs(p): return False
            
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return res if len(res) == numCourses else []