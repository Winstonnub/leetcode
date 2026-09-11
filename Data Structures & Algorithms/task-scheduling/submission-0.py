class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Idea:
        # we use a heap to store the MOST FREQUENT count, note we dont care remembering which task it is
        # we use a queue to store the task that needs to wait
        # First,  initialize the heap. Use Counter
        count = Counter(tasks) # Counter({'X': 2, 'Y': 2})
        maxHeap = [-c for c in count.values()] # An array of negative counts [-2, -2]
        heapq.heapify(maxHeap) # Heapify
        time = 0
        q = deque() # Use a queue, stores (cnt, idle time)
        while maxHeap or q:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap) # return the most frequent count -2 (then + 1)
                if c != 0:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time