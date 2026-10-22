class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Problem: Monotonic Deque
        # Why monotonic: number i before number i + 1 is going to leave the window earlier. If number i + 1 is larger, then i cannot be max anymore in its lifetime.
        # Why Deque: 
        # popleft: when index expires; pop: when new number is larger than previous one in deque
        # Algorithm:
        # 
        l = 0
        dq = deque([])
        res = []
        for r in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()
            
            if r >= k - 1:
                res.append(nums[dq[0]])
                l += 1
        return res

            
