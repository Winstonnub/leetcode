class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. SETUP
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        o = 0

        # 2. Loop through everything
        # Add ALL 'O's from the edge. We treat them as safe and BFS there, and mark all 'O's from the map that we can reach to say they are safe.
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    if ((r == 0 or r == ROWS - 1) or 
                    (c == 0 or c == COLS - 1)):
                        q.append((r,c))
        
        # 3. BFS
        while q:
            r, c = q.popleft()
            # We TURN O into T (temporary safe). At last we turn all nonT into X
            if board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and 
                        board[nr][nc] == 'O'):
                        q.append((nr,nc))
        # 4. Loop through each cell and check again
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        


