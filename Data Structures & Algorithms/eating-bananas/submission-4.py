class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles) # Bound min(piles) <= k <= max(piles)
        while l <= r: # Search for optimal mid = k
            hours = 0
            k = l + (r-l) // 2
            # Calculate how much it takes to finish if k is...
            for p in piles:
                hours += math.ceil(p/k) # if we have 5 banana and we eat 3 per hour, we need 2 hrs
            if hours <= h: # eat within h = 6 hours, but we only used 5 hours, means we can slow down
                r = k - 1
                res = min(res, k)
            else: # we have exceeded hour limit
                l = k + 1 # make k larger
        return res
                


