# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start traversing from the root node
        cur = root 

        # Continue until we find the split point
        while cur: 
            # Case 1: Both p and q are greater than current node
            # -> they must lie in the right subtree
            if p.val > cur.val and q.val > cur.val: 
                cur = cur.right

            # Case 2: Both p and q are smaller than current node
            # -> they must lie in the left subtree
            elif p.val < cur.val and q.val < cur.val: 
                cur = cur.left 

            # Case 3: Split occurs here
            # - either p and q are on different sides of cur
            # - or one of them equals cur
            # => current node is the Lowest Common Ancestor
            else: 
                return cur
