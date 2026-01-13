class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])

        # Set to keep track of cells already used in the current path
        path = set()

        # Depth First Search function
        # r, c -> current row and column
        # i -> index of current character in the word
        def dfs(r, c, i):

            # If we have matched all characters of the word
            # then we found the word
            if i == len(word):
                return True

            # If out of bounds, or character does not match,
            # or cell already used in current path → stop
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path):
                return False

            # Mark this cell as visited
            path.add((r, c))

            # Try all 4 possible directions
            res = (
                dfs(r + 1, c, i + 1) or   # down
                dfs(r - 1, c, i + 1) or   # up
                dfs(r, c + 1, i + 1) or   # right
                dfs(r, c - 1, i + 1)      # left
            )

            # Backtrack → unmark this cell so other paths can use it
            path.remove((r, c))

            return res

        # Try to start the word from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # try to match word starting here
                    return True

        return False
