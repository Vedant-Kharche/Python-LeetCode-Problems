# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We'll use an iterative inorder traversal with a stack.
        # In a BST, inorder traversal visits nodes in ascending order.
        
        stack = []        # stack to simulate recursion (keeps track of nodes)
        curr = root       # start traversal from root

        # Keep traversing until we have nodes left in stack or current pointer
        while stack or curr:
            # Step 1: Go as left as possible (push all left children)
            while curr:
                stack.append(curr)
                curr = curr.left  # move to left child

            # Step 2: Process the node at the top of the stack
            curr = stack.pop()  # this is the next smallest node in order
            k -= 1              # decrement k since we found the next smallest
            if k == 0:          # when k reaches 0, this is the kth smallest
                return curr.val
            
            # Step 3: Move to the right subtree
            curr = curr.right
