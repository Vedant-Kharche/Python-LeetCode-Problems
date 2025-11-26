class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Return the number of distinct ways to climb to step `n` when
        each move can be either 1 or 2 steps.

        Approach:
        - Use top-down DP (memoized recursion).
        - Define f(i) = number of ways to reach the top starting from step i.
        - f(i) = f(i + 1) + f(i + 2)
        - Base cases:
            * i == n -> 1 (we reached the top exactly)
            * i > n  -> 0 (we overshot the top; invalid)
        - Memoize results for indices 0..n-1 to avoid recomputation.
        """
        # Edge case: n == 0 (0 steps) — there is 1 way (do nothing).
        # This function as written already handles n == 0 correctly via the recursion base case,
        # but we can early-return for clarity.
        if n == 0:
            return 1

        # memo[i] stores the number of ways to reach the top from step i.
        # We only need slots for i in [0, n-1] because i == n is handled directly in base case.
        memo = [-1] * n

        def dfs(i: int) -> int:
            # If we've reached exactly the top, count this path as 1 valid way.
            if i == n:
                return 1
            # If we've passed the top, this path is invalid.
            if i > n:
                return 0

            # If result already computed, return it.
            if i < n and memo[i] != -1:
                return memo[i]

            # Compute the number of ways by taking 1 step or 2 steps from i.
            ways = dfs(i + 1) + dfs(i + 2)

            # Cache results only for indices within memo range (0..n-1).
            if i < n:
                memo[i] = ways

            return ways

        # Start from step 0.
        return dfs(0)
