import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0]) # rows = len of grid, cols = len of each row in grid
        visit = set()
        island = 0


        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [(1,0), (0, -1), (-1, 0), (0, 1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and 
                        (r,c) not in visit and
                        grid[r][c] == "1"):
                        q.append((r,c))
                        visit.add((r,c)) # note bfs is not recrusive so we dont run it here
                        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visit and grid[row][col] == "1":
                    bfs(row, col)
                    island += 1
        return island
                
                


