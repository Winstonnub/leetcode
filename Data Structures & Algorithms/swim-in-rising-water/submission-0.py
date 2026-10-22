class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # Idea: find the shortest path while maximum cell on the path has to be minimized (minimax djikstra's, finding the bottleneck path)
        # Signal: smallest effort / cost such that a path exist (a lot of path exist)
        # Setup: we store the max(cost, w) where cost is our current cost and w is the weight to reach that node
        # Algorithm:
            # Heap: (max(t, grid[nr][nc], nr, nc)
            # No need to loop through each t = 0,1,2,3,4...
            # Keep popping until we find our solution
            # POP: we pop and we add it's neighbours to heap
            # PUSH: just push lol
        minimaxQ = [(max(0, grid[0][0]), 0, 0)] # actual possible time to reach r, c
        n = len(grid)
        ROWS, COLS = n, n
        visited = set((0,0))
        while minimaxQ:
            time, r, c = heapq.heappop(minimaxQ)
            if (r,c) in visited:
                continue

            if (r,c) == (n-1,n-1): 
                return time
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited: 
                    heapq.heappush(minimaxQ, (max(time, grid[nr][nc]), nr, nc))
                    visited.add((r, c)) # We really 'processed this node' when we pop it here
        return -1
            
        


        
