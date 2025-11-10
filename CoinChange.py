class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array where dp[a] = minimum coins needed for amount 'a'
        # We set it to amount + 1 as a sentinel value (impossible large number)
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0 

        # Loop over all amounts from 1 to 'amount'
        for a in range(1, amount + 1):
            # Try every coin denomination
            for c in coins:
                # If the coin can contribute to the current amount
                if a - c >= 0:
                    # Update dp[a] to the minimum coins needed:
                    # Either keep current dp[a] or use this coin + dp[a-c] for remaining amount
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] was updated, return it; otherwise return -1 (no combination possible)
        return dp[amount] if dp[amount] != amount + 1 else -1