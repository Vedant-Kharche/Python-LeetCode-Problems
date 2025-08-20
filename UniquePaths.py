row = [1] * n   # Initialize a row of size 'n' filled with 1s. 
                # This represents the base case: there's only one way to move right across the last row.

for i in range(m - 1):  
    # Repeat the process (m - 1) times to simulate moving upward row by row in an m x n grid.
    
    newRow = [1] * n   # Start a new row, again with 1s (rightmost column always has only 1 way).
    
    for j in range(n - 2, -1, -1):  
        # Traverse from second last column (n-2) to the first column (0).
        # Reason: each cell depends on the cell to its right and the cell below (from previous row).
        
        newRow[j] = newRow[j + 1] + row[j]  
        # Update the number of ways:
        # newRow[j + 1] = ways to move right,
        # row[j] = ways to move down,
        # so total ways = right + down.
    
    row = newRow   # Move to the next row (going upward in the grid).

return row[0]   # Finally, return the number of ways from the top-left corner (0,0).
