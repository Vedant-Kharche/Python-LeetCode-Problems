class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Possible movement directions: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Get number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Counter to keep track of number of islands found
        islands = 0

        # BFS function to explore all land cells connected to (r, c)
        def bfs(r, c):
            q = deque()
            
            # Mark the starting cell as visited by converting "1" → "0"
            grid[r][c] = "0"
            
            # Add starting cell to the queue
            q.append((r, c))

            # Process all cells in the queue
            while q:
                row, col = q.popleft()

                # Explore neighbors in 4 directions
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # Skip if out of bounds or already water/visited
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"):
                        continue

                    # Otherwise, it's unvisited land → mark as visited
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        # Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If we find unvisited land ("1")
                if grid[r][c] == "1":
                    # Run BFS to mark the entire island as visited
                    bfs(r, c)
                    # Increase island count
                    islands += 1

        # Return total number of islands found
        return islands


# Number of Islands DFS Soln
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Directions for exploring neighbors: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Get number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        islands = 0  # Counter for number of islands

        # DFS function to explore all connected land cells
        def dfs(r, c):
            # Base case: if out of bounds OR current cell is water ("0")
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return  # Stop exploring

            # Mark current land cell as visited by turning it into water
            # This prevents revisiting the same land cell
            grid[r][c] = "0"

            # Explore all 4 neighboring cells
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Traverse each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):

                # If the cell is land ("1"), we found the start of a new island
                if grid[r][c] == "1":
                    dfs(r, c)  # Explore the entire connected island
                    islands += 1  # Increase island count

        return islands  # Return total number of islands
