class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap:
        stones = [-s for s in stones]
        heapq.heapify(stones) # Make it a max heap
        while len(stones) > 1: # while there are at least 2 nodeas
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # Case: First == Second: then do nothing, dont push back

            # Case: First > Second (since it is max heap)
            # second should be smaller (larger in negative value)
            # e.g. 10 and 5. Difference is 5.
            # first = -10, second = -5, so -10 - (-5) = -5 (first - second)
            if second > first: # negated
                heapq.heappush(stones, first - second)
        stones.append(0) # Return 0 if none remain (smallest possible is 1)
        return abs(stones[0])

