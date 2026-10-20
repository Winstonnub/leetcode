class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Problem: Min cost of connecting all nodes (Minimum Spanning Tree)
        # Algorithm: Prim's algorithm (while in_tree set < n)
        
        # Idea: keep a heap for finding shortest distance to any node we can connect out of all the nodes we have now. (cost, node)
        # Use a set to keep track of all the current points in_tree

        def dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        total = 0 
        in_tree = set() # points
        minCostHeap = [(0, 0)] # cost = 0, index of starting node is 0
        n = len(points)
        while len(in_tree) < n:
            cost, node = heapq.heappop(minCostHeap)
            if node in in_tree:
                continue
            in_tree.add(node)
            total += cost
            # Now add the new node's new distances to each remaining point into the heap
            for i in range(len(points)):
                if i in in_tree:
                    continue
                heapq.heappush(minCostHeap, (dist(points[i], points[node]), i)) # cost, node index
        return total