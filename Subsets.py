class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []       # Final list to store all subsets
        subset = []    # Temporary list to build each subset

        # Depth-First Search (DFS) recursive helper
        def dfs(i):
            # Base case: if we've considered all elements
            if i >= len(nums):
                # Append a copy of current subset (to avoid mutation issues)
                res.append(subset.copy())
                return

            # Decision 1: Include nums[i] in the subset
            subset.append(nums[i])   # choose element
            dfs(i + 1)               # move to next index

            # Backtrack: remove nums[i] to explore "exclude" option
            subset.pop()

            # Decision 2: Exclude nums[i] from the subset
            dfs(i + 1)               # move to next index

        # Start recursion from index 0
        dfs(0)

        return res   # Return all generated subsets
