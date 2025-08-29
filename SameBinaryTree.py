# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: both nodes are None -> the trees (or subtrees) are equal here
        if not p and not q:
            return True

        # Case 2: both nodes are non-None AND the values match
        # Note: the `p and q` part guarantees p and q are not None before accessing p.val.
        if p and q and p.val == q.val:
            # Recursively check left subtrees AND right subtrees.
            # The `and` means both recursive calls must return True for this node to be considered equal.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Case 3: one node is None while the other isn't, OR values differ -> trees not the same
        else:
            return False
