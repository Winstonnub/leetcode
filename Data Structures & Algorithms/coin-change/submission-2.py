class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down
        memo = {0:0}
        # Amount = 5. We PICK from coins. Then we search dp(5-coin)
        # base case
        def dp(i): # Return the min coin change needed at amount = i
            if i in memo:
                return memo[i]
            res = 1e7
            for coin in coins:
                if i - coin >= 0: # check valid next state
                    next_state = i - coin
                    candidate = 1 + dp(next_state) # we used 'coin' for 1
                    res = min(res, candidate)
            memo[i] = res
            return res
        res = dp(amount)
        return res if res < 1e7 else -1
                        
