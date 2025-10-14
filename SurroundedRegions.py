class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])

        # Helper DFS function to mark safe 'O's connected to the border
        def capture(r, c):
            # Base case: stop recursion if out of bounds or not 'O'
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return

            # Temporarily mark the cell as 'T' to indicate it's safe (connected to border)
            board[r][c] = "T"

            # Explore all 4 directions (up, down, left, right)
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Run DFS from all border 'O's to mark connected safe regions as 'T'
        for r in range(ROWS):
            if board[r][0] == "O":           # Left border
                capture(r, 0)
            if board[r][COLS - 1] == "O":    # Right border
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":           # Top border
                capture(0, c)
            if board[ROWS - 1][c] == "O":    # Bottom border
                capture(ROWS - 1, c)

        # Step 2: Flip all remaining 'O's (which are not connected to border) to 'X'
        # and restore 'T's back to 'O' (since they are safe)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"        # Surrounded region -> captured
                elif board[r][c] == "T":
                    board[r][c] = "O"        # Restore safe cell

