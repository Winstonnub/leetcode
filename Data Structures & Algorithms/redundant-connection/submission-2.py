class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find method
        # 1. Setup
        n = len(edges)
        parent = [i for i in range(len(edges)+1)]
        rank = [0] * (n+1)
        # 2. Find
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node]) # Update the parent's node
            return parent[node]
        # 3. Union
        def Union(nodeX, nodeY):
            # Smaller rank parent merge to larger rank parent
            # Same rank: then merge to latter one, add rank by to the parent
            ParentX = find(nodeX)
            ParentY = find(nodeY)
            if ParentX == ParentY:
                return False
            if rank[ParentX] < rank[ParentY]:
                parent[ParentX] = ParentY
            elif rank[ParentX] > rank[ParentY]:
                parent[ParentY] = ParentX
            else:
                parent[ParentX] = ParentY
                rank[ParentY] += 1
            return True
        
        for x,y in edges:
            # Let's try to build the edges one by one based on what we have from edges
            # When we try to add an edge between (x,y) but they have same parent, means we are making a cycle
            if not Union(x,y):
                return [x,y]
        return []
            