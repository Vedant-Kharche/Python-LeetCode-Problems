# Problem: Search in a Binary Search Tree
# Approach: Recursive and Iterative solutions using Binary Search Tree properties
# Time Complexity: O(h), where h is the height of the tree
#   - Best case: O(log N) for balanced BST
#   - Worst case: O(N) for skewed BST
# Space Complexity:
#   - Recursive: O(h) due to function call stack
#   - Iterative: O(1) constant space

class Solution(object):

    # Recursive Solution
    def searchBST(self, root, val):
        """
        Recursively searches for a node with the given value in the BST.
        If found, returns the node; else returns None.
        """

        # Base case: if current node is None, the value doesn't exist in the tree
        if root is None:
            return None

        # If current node's value matches the target, return it
        if root.val == val:
            return root

        # If target is smaller, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)

        # If target is larger, search in the right subtree
        return self.searchBST(root.right, val)

    # Iterative Solution
    def searchBST_iterative(self, root, val):
        """
        Iteratively searches for a node with the given value in the BST.
        If found, returns the node; else returns None.
        """

        temp = root  # Start traversal from the root node

        # Continue until either the node is found or we reach a leaf (None)
        while temp:
            # If the target value matches the current node, return it
            if temp.val == val:
                return temp

            # If target is greater, move to the right child
            elif temp.val < val:
                temp = temp.right

            # If target is smaller, move to the left child
            else:
                temp = temp.left

        # If we reach here, the value was not found in the BST
        return None
