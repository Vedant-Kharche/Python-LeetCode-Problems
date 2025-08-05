class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize a memoization array to store the min cost from each step
        memo = [-1] * len(cost)

        # Define a recursive function to calculate min cost from step i
        def dfs(i):
            # Base case: If we are beyond the last step, no cost to move
            if i >= len(cost):
                return 0
            
            # If result already computed, return it from memo
            if memo[i] != -1:
                return memo[i]

            # Recursive case:
            # From step i, you can go to i+1 or i+2
            # So the min cost from step i is: 
            # cost of current step + min(cost from i+1, cost from i+2)
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        # You can start at step 0 or step 1, choose the one with the lower total cost
        return min(dfs(0), dfs(1))
