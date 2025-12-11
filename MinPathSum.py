class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Number of rows (m) and columns (n)
        m, n = len(grid), len(grid[0])

        # Memoization table initialized with -1
        # dp[r][c] will store the minimum path sum from (r, c) to bottom-right
        dp = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            # Base case: if we reach the bottom-right cell,
            # return its value because there’s nowhere else to go.
            if r == m - 1 and c == n - 1:
                return grid[r][c]

            # Out-of-bound check:
            # If we move outside the grid, return +infinity (invalid path)
            if r == m or c == n:
                return float('inf')

            # If we already computed this cell before, return cached result.
            if dp[r][c] != -1:
                return dp[r][c]

            # Recursive step:
            # From current cell (r, c), you can move:
            # 1. Down → (r+1, c)
            # 2. Right → (r, c+1)
            # Choose the minimum cost path and add current cell value.
            dp[r][c] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            
            # Return and store the result for future reuse.
            return dp[r][c]

        # Start DFS from the top-left cell (0, 0)
        return dfs(0, 0)
