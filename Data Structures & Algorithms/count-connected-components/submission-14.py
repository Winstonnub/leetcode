class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Try Union Find
        # 1. Setup
        parent = [i for i in range(n)] # n nodes
        rank = [0] * n
        components = n
        
        # 2. Find
        def find(x): # Finding the parent of a node 1. Check if it is the parent already 2. Path compression 3. return
            if parent[x] == x:
                return x
            while parent[x] != find(parent[x]):
                parent[x] = find(parent[x])
            return parent[x]
        
        # 3. Union
        def Union(x,y) -> bool:
            ParentX = find(x)
            ParentY = find(y)
            if ParentX == ParentY:
                return False
            if rank[ParentX] > rank[ParentY]: # add parent y to parent x
                parent[ParentY] = parent[ParentX]
            elif rank[ParentX] < rank[ParentY]: # add parent x to parent y
                parent[ParentX] = parent[ParentY]
            else: # both rank equal so add x to y
                parent[ParentX] = parent[ParentY]
                rank[y] += 1
            return True
        
        for x, y in edges:
            if Union(x,y):
                components -= 1
        return components
