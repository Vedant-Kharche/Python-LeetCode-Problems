class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Sort coins to keep combinations in non-decreasing order
        coins.sort()

        # Memo table: memo[i][a] = number of ways to make amount 'a' using coins[i:]
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            """
            i = current index in coins
            a = remaining amount to form

            Returns the number of combinations to form amount 'a'
            using coins from index 'i' onwards.
            """

            # Base case: if amount becomes 0, we found 1 valid combination
            if a == 0:
                return 1

            # If no coins left but amount still > 0, no solution
            if i >= len(coins):
                return 0

            # Return memoized result if available
            if memo[i][a] != -1:
                return memo[i][a]

            res = 0

            # Two choices:
            # 1. Skip coin[i] → move to next coin
            # 2. Take coin[i] → stay on same coin (unlimited usage)
            if a >= coins[i]:
                # Option 1: do NOT take the coin
                res = dfs(i + 1, a)

                # Option 2: take the coin, reduce amount
                res += dfs(i, a - coins[i])
            else:
                # If coin[i] is too large, we can only skip it
                res = dfs(i + 1, a)

            # Store result in memo
            memo[i][a] = res
            return res

        # Start DFS from first coin and full amount
        return dfs(0, amount)
