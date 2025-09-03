class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get number of rows and columns in the matrix
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to store cells that can reach the Pacific and Atlantic oceans
        pac, atl = set(), set()

        # Depth-First Search (DFS) function
        def dfs(r, c, visit, prevHeight):
            # Base conditions:
            # - If this cell is already visited
            # - If we're out of bounds
            # - If current cell height < previous cell height (water can't flow uphill)
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return

            # Mark current cell as visited
            visit.add((r, c))

            # Explore all 4 directions (down, up, right, left)
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Run DFS for all cells adjacent to Pacific (top row & left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])               # Top row touches Pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Bottom row touches Atlantic

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])               # Left column touches Pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Right column touches Atlantic

        # Collect cells that can reach both Pacific AND Atlantic
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
