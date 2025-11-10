from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Queue for BFS. Each element is a cell position [r, c] that is currently rotten.
        q = deque()

        # 'time' tracks minutes elapsed (i.e., BFS levels).
        # 'fresh' tracks how many fresh oranges remain unrotted.
        time, fresh = 0, 0 

        # Dimensions of the grid (assumes at least 1 row & 1 col per problem constraints).
        rows, cols = len(grid), len(grid[0])

        # Initialize BFS:
        # - Count how many fresh oranges exist.
        # - Enqueue positions of all initially rotten oranges (multi-source BFS).
        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append([r, c])

        # 4-directional movement: right, left, down, up.
        # These are the neighbors each rotten orange can affect in 1 minute.
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # BFS proceeds level by level (each level = 1 minute of rot spread).
        # We can stop early if there are no fresh oranges left.
        while q and fresh > 0: 
            # IMPORTANT: capture the current queue size at the start of the minute.
            # Only process these many rotten oranges for this minute.
            # Any new rotten oranges appended will belong to the *next* minute.
            for _ in range(len(q)):
                r, c = q.popleft()

                # Explore the four neighbors of the current rotten orange.
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Skip out-of-bounds cells and any cell that is not a fresh orange.
                    # Valid target to rot must be exactly 1 (fresh).
                    if (row < 0 or row == rows or
                        col < 0 or col == cols or 
                        grid[row][col] != 1): 
                        continue

                    # Rot this fresh orange.
                    grid[row][col] = 2
                    # Enqueue it so it can rot its neighbors in the next minute.
                    q.append([row, col])
                    # Decrease the count of remaining fresh oranges.
                    fresh -= 1

            # Finished processing one full BFS layer -> one minute passed.
            time += 1

        # If no fresh oranges remain, 'time' is the minutes taken;
        # otherwise, some fresh oranges were unreachable -> return -1.
        return time if fresh == 0 else -1
