# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # res[0] will store the maximum path sum found so far.
        # We use a list so it can be modified inside the nested dfs function.
        res = [root.val]

        def dfs(root):
            # Base case: if the node is null, it contributes 0 to the path
            if not root:
                return 0
            
            # Recursively compute the maximum path sum from left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Update the global maximum path sum.
            # This considers a path that passes through the current node
            # and includes both left and right children.
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the maximum path sum that can be extended to the parent.
            # We can only choose one side (left or right), not both.
            return root.val + max(leftMax, rightMax)

        # Start DFS traversal from the root
        dfs(root)

        # Return the maximum path sum found in the tree
        return res[0]
