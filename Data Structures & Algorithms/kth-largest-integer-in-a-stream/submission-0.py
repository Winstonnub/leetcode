class KthLargest:
    # Min heap:
    # KEEP TRACK of k largest elements seen so far
    # If min heap has k larget, then smallest among (TOP) them is exactly the k-th largest.
    # If add new number and heap grows beyond k, remove smallest since it cannot be top k anymore (it is top k + 1)
    def __init__(self, k: int, nums: List[int]):
        # GOAL: Initialize MINHEAP with k elements (heapify, pop until only k)
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) # build the heap
        # Now we have n > k elements, keep popping until we have k elements
        # So TOP is the kth largest
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        # If heap grows beyond k, remove smallest
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]





    
