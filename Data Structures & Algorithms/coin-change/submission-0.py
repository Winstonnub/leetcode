class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Idea: we use DFS to search how much coin we need
        # Base cases
        memo = {0:0}
        
        # If amount == 0: then res = 0
        # If amount == 1: Not necessarily 1. Might not have 1
        def dp(amount): # what does dp take? the original problem parameter
            res = 1e6 # res is the smallest no. coins we need to get amount 0
            if amount in memo:
                return memo[amount]
            if amount not in memo:
                # we know that we can pick any coins, so loop thru that
                for coin in coins: # e.g. amount = 3, coins = [1,2,3]
                    # if we pick 1, then problem becomes amount = 2
                    # so answer: ONE COIN USED + Coins needed for subproblem
                    if amount - coin >= 0:
                        res = min(res, 1 + dp(amount - coin)) # what if neg?
                memo[amount] = res
            return res
        res = dp(amount)
        return res if res < 1e5 else -1
