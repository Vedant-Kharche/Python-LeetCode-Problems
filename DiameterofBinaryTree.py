# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Variable to store the maximum diameter found so far
        res = 0

        def dfs(root):
            nonlocal res  # Allows us to modify 'res' defined in the outer scope

            # Base case: if the node is None, return height 0
            if not root:
                return 0

            # Recursively compute the height of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # The diameter passing through this node is the sum of left and right subtree heights
            res = max(res, left + right)

            # Return the height of the current node
            # (1 for current node + max height of its two children)
            return 1 + max(left, right)

        # Start DFS traversal from the root
        dfs(root)

        # Return the maximum diameter found
        return res
