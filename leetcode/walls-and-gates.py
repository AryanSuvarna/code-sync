class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque() # bfs queue
        visited = set() # keep track of rooms visited

        def add_room(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append([r, c])

        # first we will add all gates to the queue first
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        # iterate on the queue
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                rooms[r][c] = dist

                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)
            
            dist += 1