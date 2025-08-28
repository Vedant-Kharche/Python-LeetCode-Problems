# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function that checks if the subtree rooted at `node` is a valid BST
        # `left` and `right` represent the valid range of values for this node
        def valid(node, left, right):
            if not node:
                # An empty subtree is always valid
                return True
            
            # Check if current node's value is within the valid range
            if not (left < node.val < right):
                return False  # Violation of BST property
            
            # Recursively check the left subtree and right subtree
            # Left subtree: all values must be < node.val
            # Right subtree: all values must be > node.val
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # Start the recursion with the whole range (-infinity to +infinity)
        return valid(root, float("-inf"), float("inf"))
