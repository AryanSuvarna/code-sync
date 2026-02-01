class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # building prerequisites adjancency list
        prereq_map = defaultdict(list)

        for c, p in prerequisites:
            prereq_map[c].append(p)
        
        # dfs for going thru all prereqs of course
        visited = set()
        def dfs(c):
            # we have detected a cycle
            if c in visited:
                return False
            
            # course has no more prereqs so we can just return True early
            if prereq_map[c] == []:
                return True

            # dfs....
            visited.add(c)
            for p in prereq_map[c]:
                if not dfs(p): return False
            visited.remove(c)

            # we've successfully parsed thru course c and its prereqs
            # set its adjancency list to [] so we avoid computing again
            prereq_map[c] = []

            return True

        
        # iterate thru every course
        for c in range(numCourses):
            if not dfs(c): return False

        # return True if we can run dfs successfully on every course
        return True