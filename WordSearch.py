class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        
        # A set to keep track of visited cells during the DFS path
        path = set()

        # Depth-First Search function
        def dfs(r, c, i):
            # Base case: if we've matched all characters in 'word'
            if i == len(word):
                return True

            # Boundary conditions and mismatches:
            # 1. r or c is out of bounds
            # 2. Current board cell doesn't match the current word character
            # 3. Current cell already visited in this search path
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # Mark the current cell as visited
            path.add((r, c))

            # Explore all 4 possible directions (up, down, left, right)
            # and move to the next character (i + 1)
            res = (
                dfs(r + 1, c, i + 1) or  # Down
                dfs(r - 1, c, i + 1) or  # Up
                dfs(r, c + 1, i + 1) or  # Right
                dfs(r, c - 1, i + 1)     # Left
            )

            # Backtrack: unmark the current cell before returning
            path.remove((r, c))
            return res

        # Try to start DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # Start searching from this cell if it matches the first letter
                if dfs(r, c, 0):
                    return True  # Found the word

        # If no starting position leads to a match, return False
        return False
