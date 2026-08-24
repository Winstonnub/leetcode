class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Standard setup
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            hours = 0
            k = l + (r - l) // 2 # rate is equal to middle
            # Loop through each entry to see how many hours it takes for k
            for p in piles:
                hours += math.ceil(p / k) # e.g. 1 / 3 takes 0.33 -> 1 hours to eat
            if hours <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res

            
            


# Idea:
# Minimum eating rate is 1.
# Maximum eating rate is the largest no. of bananas in piles.
# [1, 3, 4,7,11], h = 8
# Then 1 <= k <= 11
# For each k, we calculate the hours to finish. 
# If the calculated hours is smaller or equal to h, we search left side (smaller rate) since we have more hours to spare. Store res to be this rate. 
# If the calculated hours is larger than h, then we cannot finish the piles with k rate, so we search right side
