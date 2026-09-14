class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find Solution
        # Union means merge the smaller into larger 
        # Find means find the parent of the node
        # Rank means how many nodes is in that component if it is parent
        # 1. Setup
        #   Parents are itself [1,2,3,4,5...]
        #   Ranks are the size of its component if it is parent
        parent = [i for i in range(n)]
        rank = [0] * n

        # 2. Define Find
        def find(node):
            # If the node's parent is not itself, we set node's parent to be find node's parent
            if node != parent[node]:
                parent[node] = find(parent[node]) # Recursively find root
            return parent[node]
        
        # 3. Define Union
        # To Union two nodes, we compare their parents Rank.
        # If two nodes parent are identical, do nothing.
        # For the one with smaller rank, we link that to the larger rank
        # If two nodes parent have same rank, add Parent of Y to Parent of X, increase X rank by 1.
        def union(x, y):
            ParentX = find(x)
            ParentY = find(y)
            if ParentX == ParentY:
                return False
            if rank[ParentX] < rank[ParentY]:
                parent[ParentX] = ParentY
            elif rank[ParentY] < rank[ParentX]:
                parent[ParentY] = ParentX
            else:
                parent[ParentY] = ParentX
                rank[ParentX] += 1
            return True
        
        for n1, n2 in edges:
            # For each Union, we make a component and form edge.
            # An edge decrease no. components by 1.
            # SO answer is (n subtracted by no. edges made from Union).
            if union(n1,n2) == True:
                n -= 1
        return n

            

