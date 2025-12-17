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

#TOP DOWN APPROACH
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization dictionary to store the minimum coins needed
        # for a given remaining amount
        memo = {}

        def dfs(amount):
            # Base case: if amount is 0, no coins are needed
            if amount == 0:
                return 0

            # If this amount has already been computed, return cached result
            if amount in memo:
                return memo[amount]

            # Initialize result with a large number (acts as infinity)
            res = 1e9

            # Try using each coin
            for coin in coins:
                # Only proceed if coin value does not exceed the amount
                if amount - coin >= 0:
                    # Recursively compute coins needed for remaining amount
                    # Add 1 for the current coin used
                    res = min(res, 1 + dfs(amount - coin))

            # Store the computed minimum coins for this amount
            memo[amount] = res
            return res

        # Compute minimum coins needed for the full amount
        minCoins = dfs(amount)

        # If result is still infinity, it's not possible to form the amount
        return -1 if minCoins >= 1e9 else minCoins
