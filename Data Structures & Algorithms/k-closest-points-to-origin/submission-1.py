import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Similar to the kth largest problem
        # In a min heap of k elements, the top is the kth largest
        # Idea:
        # 1. Augment points. For each point, augment with distance. Then heapify points. Now it might have more than k elements
        # 2. We pop elements until it has k elements.
        # 3. Then we pop every element in the heap to get the solution
        points = [[math.sqrt((x)**2 + (y)**2), x, y] for x, y in points]
        heapq.heapify(points)
        res = []
        for i in range(k):
            res.append(heapq.heappop(points)[1:3])
        return res