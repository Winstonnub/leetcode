class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # Biggest Takeaway: Use the coin or not use it?
        # 1. State
            # dp[i][a]:
            # Given coin types up to i (so current c = coin[i-1]), how many ways can we obtain amount a?
        # 2. Transition: To obtain amount a, we either
            # 1. find the no. ways to obtain a-c with given coin types up to i (Using coin c, only if a >= c)
            # - dp[i][a-c]
            # 2. find the current no. ways to obtain a with given coin types up to i - 1 (Not using coin c)
            # - dp[i-1][a]
            #
        # 3. Base Case
        # For amount 0, we pick nothing.
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]  # dp[i] means ith coin, dp[0] means no coin
        for i in range(len(coins) + 1): 
            dp[i][0] = 1 
        for i in range(1, len(coins) + 1): # For each coin
            coin = coins[i-1] # e.g the ith coin is index i-1
            for a in range(0, amount + 1): # for each amount that is greater than coin (so coin actually be used)
                if a >= coin:
                    dp[i][a] = dp[i][a-coin] + dp[i-1][a]
                else:
                    dp[i][a] = dp[i-1][a]
        return dp[len(coins)][amount]

