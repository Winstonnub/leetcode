class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1. Define setup
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [(0,1), (1,0), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and (r,c) not in visited and grid[r][c] == 1):
                        area += 1
                        q.append((r,c))
                        visited.add((r,c))
            return area
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea

            



