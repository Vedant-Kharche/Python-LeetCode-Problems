class Solution:
    def numSquares(self, n: int) -> int:
        # Dictionary to store previously computed results for memoization
        memo = {}

        def dfs(target):
            # Base case: if target is 0, no more squares are needed
            if target == 0:
                return 0

            # If the result for this target is already computed, return it
            if target in memo:
                return memo[target]

            # Initialize result with the worst case (using '1' repeatedly)
            # e.g., for n=12, worst case is 12 (1^2 + 1^2 + ... + 1^2)
            res = target

            # Try every square number less than or equal to target
            for i in range(1, target + 1):
                # Stop when i^2 exceeds target
                if i * i > target:
                    break

                # Recursively compute the minimum number of squares needed
                # after subtracting i^2 from the target
                # Add 1 because we're using one square (i^2)
                res = min(res, 1 + dfs(target - i * i))

            # Store the computed result in memo to avoid recalculating
            memo[target] = res
            return res

        # Start DFS from the given number n
        return dfs(n)
