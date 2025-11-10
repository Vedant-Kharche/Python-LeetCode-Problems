class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # Initialize boundaries
        left, right = 0, len(matrix[0])     # leftmost and rightmost column indices
        top, bottom = 0, len(matrix)        # topmost and bottommost row indices

        # Keep looping until the boundaries overlap
        while left < right and top < bottom:

            # 1. Traverse from left to right along the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1   # move the top boundary down (top row is processed)

            # 2. Traverse from top to bottom along the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1   # move the right boundary left (right column is processed)

            # Check if we still have rows and columns left
            if not (left < right and top < bottom):
                break

            # 3. Traverse from right to left along the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1   # move the bottom boundary up (bottom row is processed)

            # 4. Traverse from bottom to top along the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1   # move the left boundary right (left column is processed)

        return res
