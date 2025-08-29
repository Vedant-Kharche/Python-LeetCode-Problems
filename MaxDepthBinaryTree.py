# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Use a stack for DFS (iterative approach).
        # Each element in the stack is [node, current_depth]
        stack = [[root, 1]]

        # Variable to store the maximum depth found so far
        res = 0

        # Traverse while there are nodes in the stack
        while stack:
            # Pop a node and its depth from the stack
            node, depth = stack.pop()

            if node:  # Only process non-null nodes
                # Update result with the maximum depth seen so far
                res = max(res, depth)

                # Add the left child with depth + 1
                stack.append([node.left, depth + 1])

                # Add the right child with depth + 1
                stack.append([node.right, depth + 1])

        # Return the maximum depth
        return res
