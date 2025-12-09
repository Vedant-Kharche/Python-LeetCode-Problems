class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Total rows and columns in the board
        ROWS, COLS = len(board), len(board[0])

        # A set to track the cells we are currently visiting in the DFS path
        # This prevents revisiting the same cell in the same path (no reuse of characters)
        path = set()

        def dfs(r, c, i):
            """
            r, c => current cell coordinates
            i    => index of current character in 'word' we are trying to match
            """

            # BASE CASE:
            # If we've matched every character in 'word', return True
            if i == len(word):
                return True

            # BOUNDARY + VALIDATION CHECKS:
            # 1. Out of bounds?
            # 2. Does board[r][c] NOT match the word's current character?
            # 3. Have we already visited this cell in the current path?
            if (min(r, c) < 0 or                  # r < 0 or c < 0
                r >= ROWS or c >= COLS or        # out of bounds
                word[i] != board[r][c] or        # char mismatch
                (r, c) in path):                 # already visited
                return False

            # Add current cell to path => marking it as visited for this DFS branch
            path.add((r, c))

            # Explore all 4 possible directions for the next character:
            # Down, Up, Right, Left
            res = (
                dfs(r + 1, c    , i + 1) or
                dfs(r - 1, c    , i + 1) or
                dfs(r    , c + 1, i + 1) or
                dfs(r    , c - 1, i + 1)
            )

            # BACKTRACK:
            # Remove the cell from the path when returning so other branches can use it
            path.remove((r, c))

            return res

        # Try starting the DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # If any DFS path returns True, the word exists in the board
                if dfs(r, c, 0):
                    return True

        # If no starting point matched the entire word
        return False
