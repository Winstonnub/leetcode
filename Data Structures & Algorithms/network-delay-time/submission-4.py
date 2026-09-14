class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djikstra's Algorithm
        # 1. Setup
        neighbours = defaultdict(list)
        visited = set()
        for u, v, t in times:
            neighbours[u].append((t,v)) # [time it takes, point to where]
        
        # 2. Run on MinHeap
        minHeap = [(0,k)] # [Time it takes total, point to where]
        res = 0
        while minHeap:
            # Pop the node from minHeap
            # If we already visited this node, skip
            # Set the time to be the time to travel to this node (guaranteed minimum since it was from minheap)
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res = time
            # Push new ones in
            for newTime, newNode in neighbours[node]:
                heapq.heappush(minHeap, (time + newTime, newNode)) # how long it takes to get to newNode, newNode
        return res if len(visited) == n else -1





        