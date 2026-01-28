class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # make adjancency list for each course (course : [prereqs])
        prereq_map = defaultdict(list)

        for c, p in prerequisites:
            prereq_map[c].append(p)
        

        output = []
        visited = set()
        cycle = set()
        def dfs(c):
            # we've already seen this course in the cycle
            if c in cycle:
                return False
            # we've already seen this course and we know it is a valid
            if c in visited:
                return True
            
            # dfs ....


            cycle.add(c)
            # run dfs on each prereq
            for p in prereq_map[c]:
                if not dfs(p): return False
            cycle.remove(c)
            
            # we've gone thru all prereqs with no issues, meaning we can take this course if we have taken all the prereqs first
            visited.add(c)
            output.append(c)

            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return output if len(output) == numCourses else []