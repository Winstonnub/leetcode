class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Min Heap Solution
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = [] # Use min heap, remove when find larger
        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap) # smallest count[num] currently
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


            
            
