class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0]) # 1. Define rows, cols, visit sets 
        pac, atl = set(), set() 

        # 2. Define DFS: we go from the side, and do dfs on each direction to add all nodes in visit (pac or atl)
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or # Don't revisit
              r < 0 or c < 0 or # Don't go out of bound
              r == ROWS or c == COLS or 
              heights[r][c] < prevHeight # Not reachable from previous cell
            ):
                return
            visit.add((r, c)) # mark as reachable from previous cell
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # 3. Run through the boundaries
        #DFS: does not travel if in visit, out of bound, or this height is smaller than previous (we go from sea to ground)
        for c in range(COLS): # for all columns in row 0 and last row
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS): # for all rows in col 0 and last col
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        # 4. Find all cells in pac and atl, then append to res.
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        return res
            