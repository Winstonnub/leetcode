class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n, m = len(grid), len(grid[0])
        q = deque()
        INF = 2 ** 31 - 1 # float("inf")

        # Find treasures in O(nm) time
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append( (r, c) )

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q :

            r, c = q.popleft()

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if ( 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == INF ) :
                    q.append( [new_r, new_c] )
                    grid[new_r][new_c] = grid[r][c] + 1


