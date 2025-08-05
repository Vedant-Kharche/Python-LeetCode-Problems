class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a cache (memoization array) of size n initialized with -1.
        # cache[i] will store the number of ways to reach the top from step i.
        cache = [-1] * n

        # Define a recursive DFS function that starts at step i
        def dfs(i):
            # Base case: If we've gone past the last step, no valid way (return 0)
            # But if we're exactly on the last step (i == n), it is one valid way
            if i >= n:
                return i == n  # True (1) if i == n, else False (0)

            # If we've already computed this subproblem, return the cached result
            if cache[i] != -1:
                return cache[i]

            # Recursive case:
            # The number of ways to reach the top from step i is the sum of:
            # - ways from i+1 (taking 1 step)
            # - ways from i+2 (taking 2 steps)
            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        # Start the recursion from step 0
        return dfs(0)
