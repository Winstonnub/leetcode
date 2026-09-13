class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = set() # Visited
        ROW, COL = len(board), len(board[0])
        # RUN BFS
        def dfs(r, c, i):
            # Base Case: we reach the end of i
            if i == len(word):
                return True
            # We don't proceed if
            # 1. Invalid entry r >= ROW, r < 0
            # 2. Invalid entry c >= col, c < 0
            # 3. Visited, the (r,c) is in cur
            # 4. The word is NOT what we looking for
            if (r >= ROW or c >= COL or 
                r < 0 or c < 0 or
                (r,c) in cur or
                board[r][c] != word[i]):
                return False
            # We proceed now by checking all paths (left right up down)
            cur.add((r,c)) # We visited this path
            res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            cur.remove((r,c)) # We unvisit this path 
            return res
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0): return True
        return False
                 
                
        
        
            

        
        