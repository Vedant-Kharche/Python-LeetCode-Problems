class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # l and r are pointers to the current "layer" (left and right boundaries)
        l, r = 0, len(matrix) - 1  

        # Keep processing until left crosses right (layer by layer)
        while l < r:
            # Traverse each element in the current layer (except the last, handled by loop)
            for i in range(r - l):
                top, bottom = l, r  # define the top and bottom row indices of this layer

                # 1️⃣ Save the top-left value (because it will be overwritten)
                topLeft = matrix[top][l + i]

                # 2️⃣ Move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # 3️⃣ Move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # 4️⃣ Move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # 5️⃣ Move saved top-left → top-right
                matrix[top + i][r] = topLeft

            # Shrink the boundaries inward (move to the next inner layer)
            r -= 1
            l += 1
