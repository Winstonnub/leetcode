class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Use BFS and check every cell!
        # Step 1. Setup (This time visited is in bfs, since we will revisit)
        # Step 2. Define BFS (queue, 4 conditions, visited)
        # Step 3. for r,c in each cell
        # NO. NOT OPTIMAL ENOUGH. USE MULTI-SOURCE BFS 
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


        

