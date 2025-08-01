from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]      # 2D grid representing the maze
        :type entrance: List[int]        # Starting cell [row, col]
        :rtype: int                      # Minimum steps to the nearest exit, or -1 if not found
        """
        
        # Initialize a queue for BFS and start from the entrance cell with 0 steps
        cells = deque([(entrance[0], entrance[1], 0)])
        
        # Mark the entrance as visited to avoid revisiting
        maze[entrance[0]][entrance[1]] = "+"

        rows, cols = len(maze), len(maze[0])  # Dimensions of the maze

        # Start BFS loop
        while cells:
            r, c, steps = cells.popleft()  # Current cell (r, c) and number of steps taken

            # Check all four possible directions: down, up, right, left
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                
                # Check if the next cell (i, j) is inside the maze and is an open path ('.')
                if 0 <= i < rows and 0 <= j < cols and maze[i][j] == ".":
                    
                    # If this cell is on the boundary and is not the entrance, it's an exit
                    if [i, j] != entrance and (i == 0 or j == 0 or i == rows - 1 or j == cols - 1):
                        return steps + 1  # Exit found, return number of steps taken

                    # Otherwise, add the cell to the queue to continue BFS
                    cells.append((i, j, steps + 1))

                    # Mark the cell as visited to avoid revisiting
                    maze[i][j] = "+"

        # If no exit is reachable, return -1
        return -1
