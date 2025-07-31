# Problem: Delete Node in a Binary Search Tree
# Approach: Recursive BST deletion handling all cases (leaf, one child, two children)
# Time Complexity: O(h), where h is the height of the tree
#   - O(log N) for balanced BST, O(N) for skewed BST
# Space Complexity: O(h) due to recursive call stack

class Solution(object):
    def deleteNode(self, root, key):
       
        # Base case: If the root is None, return None (nothing to delete)
        if not root:
            return root

        # If the key is greater, move to the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If the key is smaller, move to the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If key == root.val, we've found the node to delete
        else:
            # Case 1: Node has no left child, return right child
            if not root.left:
                return root.right

            # Case 2: Node has no right child, return left child
            elif not root.right:
                return root.left

            # Case 3: Node has two children
            # Find the in-order successor (minimum value in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left

            # Replace current node's value with in-order successor's value
            root.val = curr.val

            # Recursively delete the in-order successor node from right subtree
            root.right = self.deleteNode(root.right, root.val)

        # Return the updated root
        return root
