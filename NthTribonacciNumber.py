class Solution:
    def __init__(self):
        # Dictionary used for memoization (caching previously computed results)
        # Helps avoid recomputing the same Tribonacci numbers multiple times
        self.dp = {}

    def tribonacci(self, n: int) -> int:
        # ---------------- BASE CASES ----------------
        # According to the Tribonacci definition:
        # T(0) = 0
        # T(1) = 1
        # T(2) = 1
        if n <= 2:
            return 1 if n != 0 else 0

        # ---------------- MEMOIZATION CHECK ----------------
        # If we have already computed tribonacci(n),
        # return the stored result instead of recomputing
        if n in self.dp:
            return self.dp[n]

        # ---------------- RECURSIVE RELATION ----------------
        # Tribonacci formula:
        # T(n) = T(n-1) + T(n-2) + T(n-3)
        self.dp[n] = (
            self.tribonacci(n - 1) +
            self.tribonacci(n - 2) +
            self.tribonacci(n - 3)
        )

        # Return the cached result
        return self.dp[n]
