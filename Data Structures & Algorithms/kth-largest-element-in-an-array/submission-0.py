class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Basically want to find the Kth largest element
        # Remember: For a heap of k elements, the min heap of it is the kth largest
        # So: Initialize the heap, heapify with nums, then heappop until it reaches k elements
        # After that, we pop it
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return heapq.heappop(nums) 