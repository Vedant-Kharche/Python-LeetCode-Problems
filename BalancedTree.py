# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function: returns [isBalanced, height] for the current subtree
        def dfs(root):
            # Base case: if the node is None, it's balanced with height 0
            if not root:
                return [True, 0]

            # Recursively check left and right subtrees
            left = dfs(root.left)   # [balanced?, height]
            right = dfs(root.right) # [balanced?, height]

            # A node is balanced if:
            #   1. Its left subtree is balanced
            #   2. Its right subtree is balanced
            #   3. The height difference between left and right is <= 1
            balanced = (
                left[0] and 
                right[0] and 
                abs(left[1] - right[1]) <= 1
            )

            # Height of current node = 1 + max(left height, right height)
            return [balanced, 1 + max(left[1], right[1])]

        # Start DFS from root and return only the balance status
        return dfs(root)[0]
