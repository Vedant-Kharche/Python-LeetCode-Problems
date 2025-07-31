class Solution(object):
    def maxLevelSum(self, root):
        # Edge case: if the tree is empty, return 0
        if not root:
            return 0

        # Initialize the queue with the root node (used for level order traversal)
        q = [root]

        # Track the level with the maximum sum (starting from level 1)
        max_level = 1
        # Current level number
        level = 1
        # Initialize the maximum sum with negative infinity to ensure any real sum will be higher
        max_sum = float('-inf')

        # Perform level-order traversal (BFS)
        while q:
            level_sum = 0  # Sum of values at the current level
            next_level = []  # List to store nodes for the next level

            # Iterate through all nodes at the current level
            for node in q:
                # Add the node's value to the current level sum
                level_sum += node.val

                # If left child exists, add it to the queue for the next level
                if node.left:
                    next_level.append(node.left)
                # If right child exists, add it to the queue for the next level
                if node.right:
                    next_level.append(node.right)

            # If the sum of the current level is greater than the max sum seen so far,
            # update max_sum and the corresponding level
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            # Move to the next level
            q = next_level
            level += 1

        # Return the level number with the maximum sum
        return max_level
