# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree (or subtree) is empty, return None
        if not root:
            return None

        # Swap the left and right child of the current node
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree
        self.invertTree(root.left)

        # Recursively invert the right subtree
        self.invertTree(root.right)

        # Return the root node after inverting its children
        return root
