class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Problem: Determine if the array can be partitioned into two subsets with equal sum.
        Approach: 
        - Use DFS (Depth-First Search) with memoization to explore possible subset sums.
        - The goal is to find a subset whose sum equals total_sum / 2.
        """

        # Step 1: Compute the total sum of all numbers
        total = sum(nums)

        # If total sum is odd, we cannot split it into two equal integer parts
        if total % 2 != 0:
            return False

        # Step 2: Target sum for one subset (the other subset will automatically have the same sum)
        target = total // 2
        n = len(nums)

        # Step 3: Initialize memoization table
        # memo[i][t] = whether we can achieve sum 't' using elements from index i onward
        # -1 means not yet computed, True/False once computed
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        # Step 4: Define recursive DFS function
        def dfs(i, target):
            """
            Returns True if we can reach 'target' sum starting from index i.
            """
            # Base case: target reached → valid subset found
            if target == 0:
                return True
            # Base case: exhausted all numbers or target went negative → invalid path
            if i >= n or target < 0:
                return False

            # If already computed, return stored result to avoid recomputation
            if memo[i][target] != -1:
                return memo[i][target]

            # Recursive choices:
            # 1️⃣ Skip current number → dfs(i + 1, target)
            # 2️⃣ Include current number → dfs(i + 1, target - nums[i])
            memo[i][target] = (
                dfs(i + 1, target) or 
                dfs(i + 1, target - nums[i])
            )

            return memo[i][target]

        # Step 5: Start DFS from index 0, looking for subset sum = target
        return dfs(0, target)
