class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # --- Step 1: Binary search to find the correct row ---
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2  # Middle row
            # If target is greater than the last element in this row,
            # the target must be in a lower row
            if target > matrix[row][-1]:
                top = row + 1
            # If target is smaller than the first element in this row,
            # the target must be in an upper row
            elif target < matrix[row][0]:
                bot = row - 1
            # Otherwise, the target is within the range of this row
            else:
                break

        # If no valid row found, target is not in matrix
        if not (top <= bot):
            return False

        # After loop: row is the candidate row where target could be
        row = (top + bot) // 2

        # --- Step 2: Binary search inside the chosen row ---
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2  # Middle column index
            if target > matrix[row][m]:
                l = m + 1   # Search right half
            elif target < matrix[row][m]:
                r = m - 1   # Search left half
            else:
                return True  # Found target

        # If loop finishes, target is not present
        return False
