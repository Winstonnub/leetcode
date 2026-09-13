class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Use Multi-Source BFS and check every cell!
        # Step 1. Setup (This time visited is in bfs, since we will revisit)
        # Step 2. for r,c in each cell: we append the source to the queue
        # Step 3. while q: 
                    # main thing is using the last cell's VALUE + 1

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        step = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c)) # MULTI SOURCE BFS!
        while q:
            # IN THIS LAYER PARTICULARLY!
            row, col = q.popleft()
            directions = [(-1,0), (1,0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == INF):
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))


        

