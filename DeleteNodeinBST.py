# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # ✅ BASE CASE:
        # If the tree is empty, return None
        if not root:
            return root

        # ✅ STEP 1: SEARCH FOR THE NODE TO DELETE
        # If key is greater than current node value → go RIGHT
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If key is smaller than current node value → go LEFT
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # ✅ STEP 2: NODE FOUND (key == root.val)
        else:

            # ✅ CASE 1: Node has NO LEFT child
            # Replace node with its RIGHT child
            if not root.left:
                return root.right

            # ✅ CASE 2: Node has NO RIGHT child
            # Replace node with its LEFT child
            elif not root.right:
                return root.left

            # ✅ CASE 3: Node has TWO children
            # Find the inorder successor (smallest value in right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left

            # Replace root's value with successor's value
            root.val = cur.val

            # Delete the successor node from right subtree
            root.right = self.deleteNode(root.right, root.val)

        # ✅ Return updated root
        return root
