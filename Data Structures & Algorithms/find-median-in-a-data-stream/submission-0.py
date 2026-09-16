class MedianFinder:
    # Idea is: 
    # Make two heaps.
    # First heap stores the smaller part with MaxHeap
    # Second heap stores the bigger part with minHeap
    # e.g. [1] then [1]
    # [1,2] then [1] [2]
    # [1,2,3] then [1,2] [3]
    # [1,2,3,4] then [1,2] [3,4]
    # [1,2,3,4,5] then [1,2,3] [4,5]
    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]: #if there is large, and num >= smallest in large
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num) # we push if there is no large
        # Rebalance: if one heap becomes larger than other by more than 1, move top to other heap
        if len(self.large) - len(self.small) > 1:
            top = heapq.heappop(self.large)
            heapq.heappush(self.small, -top)
        elif len(self.small) - len(self.large) > 1:
            top = -heapq.heappop(self.small)
            heapq.heappush(self.large, top)
        
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])
        elif len(self.large) < len(self.small):
            return float(-self.small[0])
        else:
            return (self.large[0] - self.small[0]) / 2.0
        
        
        