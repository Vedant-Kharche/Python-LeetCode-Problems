# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: no nodes left
        if not preorder or not inorder:
            return None 
        
        # First element in preorder is always the root
        root = TreeNode(preorder[0])
        
        # Find the index of root in inorder (splits left/right subtree)
        mid = inorder.index(preorder[0])
        
        # Build left subtree
        # preorder[1:mid+1] → next 'mid' nodes (left subtree nodes)
        # inorder[:mid] → all elements before root in inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Build right subtree
        # preorder[mid+1:] → remaining nodes after left subtree
        # inorder[mid+1:] → all elements after root in inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
