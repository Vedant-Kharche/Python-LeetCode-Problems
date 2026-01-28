class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Step 1: Calculate the total sum of all numbers
        total = sum(nums)

        # If the total sum is odd, it cannot be split into two equal halves
        # because two equal integers cannot add up to an odd number
        if total % 2 != 0:
            return False

        # Step 2: Each subset must sum to half of the total
        target = total // 2

        # Number of elements in the list
        n = len(nums)

        # Step 3: Create a memoization table
        # memo[i][t] stores:
        #   - True  → if we can form sum 't' using elements from index i onward
        #   - False → if we cannot
        #   - -1    → state has not been computed yet
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        # Step 4: Depth-First Search with memoization
        def dfs(i, target):
            # Base Case 1:
            # If target becomes 0, we have found a valid subset
            if target == 0:
                return True

            # Base Case 2:
            # If we've used all elements OR target becomes negative,
            # this path cannot form the required sum
            if i >= n or target < 0:
                return False

            # If this subproblem was already solved, return stored result
            if memo[i][target] != -1:
                return memo[i][target]

            # Choice 1: Skip the current number nums[i]
            # Choice 2: Include the current number nums[i] in the subset
            memo[i][target] = (
                dfs(i + 1, target) or          # Exclude nums[i]
                dfs(i + 1, target - nums[i])   # Include nums[i]
            )

            # Store and return the result for this state
            return memo[i][target]

        # Step 5: Start DFS from index 0 with the full target sum
        return dfs(0, target)
