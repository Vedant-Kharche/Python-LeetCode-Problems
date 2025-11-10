class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the bottom row of the grid with 1s.
        # Each cell has only 1 way to reach the destination (by moving right).
        row = [1] * n  

        # Loop through the remaining (m - 1) rows from bottom to top
        for i in range(m - 1):
            # Start a new row with all 1s (since the rightmost cell always has 1 way).
            newRow = [1] * n  

            # Traverse the row from right to left, filling in number of paths.
            for j in range(n - 2, -1, -1):  
                # The number of ways to reach the destination from this cell
                # = ways from the cell to the right + ways from the cell below
                newRow[j] = newRow[j + 1] + row[j]

            # Move up to the next row
            row = newRow  

        # The top-left cell contains the total number of unique paths
        return row[0]  
