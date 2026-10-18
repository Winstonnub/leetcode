class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        # STATE: dp[r][c] is the longest increasing path starting at matrix[i][j] (value is integer)
        # Transition:
        # dp[r][c] = 1 + max(dp[r+dr][c+dc] for dr, dc in [(0,1), ...])
        # Base case: Each starting point is 1 if it is a peak?
        # Use DFS to fill in the memo (DP) in demand 
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        def dfs(r,c) -> int:
            if dp[r][c] != 0:
                return dp[r][c]
            dp[r][c] = 1
            directions = [(0,1), (1,0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and matrix[nr][nc] > matrix[r][c]:
                    if dp[nr][nc] == 0:
                        dp[nr][nc] = dfs(nr,nc)
                    dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])
            return dp[r][c]
        for r in range(ROWS):
            for c in range(COLS):
                if dp[r][c] == 0:
                    dp[r][c] = dfs(r,c)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dp[r][c])
        return res

            
        
