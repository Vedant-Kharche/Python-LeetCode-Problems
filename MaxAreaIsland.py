class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # A set to track visited cells so we don’t count the same land twice
        visit = set()

        # Depth-First Search (DFS) to explore an island starting from (r, c)
        def dfs(r, c):
            # Base case: return 0 if:
            # - Out of grid bounds
            # - Cell is water (0)
            # - Already visited this land cell
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit):
                return 0

            # Mark current land cell as visited
            visit.add((r, c))

            # Count current cell (1) + area of all connected neighbors (up, down, left, right)
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        # Track the largest island area found
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                # Start DFS if the cell is land and not yet visited
                area = max(area, dfs(r, c))

        # Return the maximum area among all islands
        return area
