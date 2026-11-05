class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Djkstra's
    # build adjacency list
    # minheap (cost, node)
    # if cost + neighbour edge > distance[nei]:
        # then update distance[nei]
    # return max(dist)
        dist = [float("inf")] * (n+1) # O(V) where |V| = n
        dist[k] = 0
        adj = defaultdict(list)
        for u,v,c in times: # for each edge O(E)
            adj[u].append((c,v)) #cost, node v

        q = [(0, k)] # at node k, cost to reach itself is 0
        while q:
            cost, currNode = heapq.heappop(q)
            if cost != dist[currNode]: # we skip since it was updated before us, someone else got better path already
                continue 
            dist[currNode] = cost
            for neiEdgeCost, neiNode in adj[currNode]:
                if cost + neiEdgeCost < dist[neiNode]: 
                    # we have a faster way to get there!
                    dist[neiNode] = cost + neiEdgeCost
                    heapq.heappush(q, (cost + neiEdgeCost, neiNode))
        result = max(dist[1:])
        return -1 if result == float("inf") else result

                 


    

    