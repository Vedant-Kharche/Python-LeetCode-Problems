class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        # set to keep track of visited cells (r, c)
        visit = set()
        # queue for BFS; we'll store coordinates as lists [r, c] (could be tuples)
        q = deque()

        def addCell(r, c):
            """
            Helper to try to add a neighbor cell to the BFS queue.
            It prevents out-of-bounds, revisiting, and obstacles (-1).
            """
            # check row/col bounds, revisited cells, or obstacle
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            # mark visited and push onto queue
            visit.add((r, c))
            q.append([r, c])

        # Initialize the BFS queue with all source cells (cells equal to 0).
        # These are the starting points for the multi-source BFS.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # dist will represent the distance from the nearest 0 for the current "layer"
        dist = 0
        # Perform level-order BFS: process the whole layer, then increment distance.
        while q:
            # process every cell currently in the queue (this is one BFS layer)
            for i in range(len(q)):
                r, c = q.popleft()
                # write the distance into the grid in-place
                grid[r][c] = dist
                # try to add the four orthogonal neighbors
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            # after processing the whole layer, increase distance for next layer
            dist += 1