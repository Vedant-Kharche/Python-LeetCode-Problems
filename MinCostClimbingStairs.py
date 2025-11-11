class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create a memoization array to store the minimum cost from each step.
        # Initialized with -1 meaning "not yet computed".
        memo = [-1] * len(cost)

        # Define a recursive helper function that returns
        # the minimum cost to reach the top starting from step i.
        def dfs(i):
            # Base case: if we go beyond the last step, cost is 0
            # because we've reached the top.
            if i >= len(cost):
                return 0

            # If we already computed the minimum cost from step i,
            # return it to avoid recomputation (memoization).
            if memo[i] != -1:
                return memo[i]

            # Recursive case:
            # From step i, we can either climb 1 or 2 steps.
            # We add the cost of the current step to the minimum cost
            # of the next possible moves (i+1 or i+2).
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            # Return the computed minimum cost for step i.
            return memo[i]

        # The starting point can be either step 0 or step 1.
        # We take the minimum total cost between starting at 0 or 1.
        return min(dfs(0), dfs(1))
