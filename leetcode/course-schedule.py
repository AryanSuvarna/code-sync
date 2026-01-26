class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        
        visited = set()

        def dfs(c):
            # we have a loop (impossible to learn all courses)
            if c in visited:
                return False
            
            # curr course has no prereqs so just return true
            if prereq_map[c] == []:
                return True
            
            # explore the prereqs of current course
            
            # explore course
            visited.add(c)
            # run dfs on prereqs
            for pre in prereq_map[c]:
                if not dfs(pre): return False
            
            # remove it and set preq map to empty as we have proven it is possible to visit all prereqs
            visited.remove(c)
            prereq_map[c] = []
            return True
        
        # now run dfs on all courses and return true if all courses are possible to take
        for c in range(numCourses):
            if not dfs(c): return False
        
        return True