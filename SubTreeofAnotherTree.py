# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty (None), it's always a subtree of any tree
        if not subRoot:
            return True
        # If root is empty but subRoot is not, then subRoot can't be a subtree
        if not root:
            return False

        # Check if the current root and subRoot are the same tree
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check left and right subtrees of root
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees match at this branch
        if not root and not subRoot:
            return True
        # If both nodes exist and values are equal, check their children recursively
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        # Otherwise (one is None or values don't match), not the same tree
        return False
