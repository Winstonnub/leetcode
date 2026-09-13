class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # We use BFS
        # We run BFS on ALL cells
        # we add res after each successful BFS in each cell
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, -1), (-1,0), (0, 1)]
        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        (r,c) not in visited and
                        grid[r][c] == '1'):
                        q.append((r,c))
                        visited.add((r,c))
                    
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1
        return islands
                
                    


            