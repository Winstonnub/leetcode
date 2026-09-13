class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-Source BFS!
        # 1. Setup (ROWS, COLS, RES, VISITED)
        # 2. Initiate bfs by putting each source into a queue (rmb step)
        # 3. BFS
        # MISTAKE: Did not count fresh, lead to one over count loop
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1), (1, 0), (-1,0), (0,-1)]

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        step = 0
        while q and fresh > 0: # avoid counting one more bfs even theres no step
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and grid[nr][nc] == 1):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            step += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return step
            
            

