class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Bellman-ford's algorithm bounded by k: minimum cost in a directed graph 
            # Shortest paths by repeated rounds of 'relax every edge', after round i, price[v] = cheapest way to reach v using at most i edges
        # State: prices[dst] returns the cheapest price to reach dst from src, after allowing k + 1 edges at max.
        # Transition:
        # tmp[u] + cost < prices[v] # If current cheapest price is larger, update. 
        # we need to use tmp = prices.copy(). We want to use cheapest price from last round, so that we are not using our current prices (possibility of making multiple flights).

        # Algo:
        # 1. Set all arrival time to be infinity and 0 on source
        # 2. For max k edges,
            # We save a copy of our arrival times at i edges
            # Then for each transition edges we have (u,v,cost), we check and update
            # tmp[u] + price < prices[v]: if min cost reaching u + u->v cost < min cost to reach v
        # 3. return -1 if destination is inf, else that arrival time
        # No heap is needed. Just updating dp array that keep track of min cost at 'expanded to max kth edges'

        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(0, k + 1):
            tmp = prices.copy()
            for u, v, price in flights:
                if tmp[u] == float("inf"):
                    continue
                if tmp[u] + price < prices[v]:
                    prices[v] = tmp[u] + price
            
        return -1 if prices[dst] == float("inf") else prices[dst]



        
