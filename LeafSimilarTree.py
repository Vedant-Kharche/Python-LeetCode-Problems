class Solution(object):
    def leafSimilar(self, root1, root2):
        #function to perform DFS and collect leaf node values
        def dfs(root, leaf):
            if not root:
                return  # Base case: if the node is None, do nothing
            if not root.left and not root.right:
                # If the node is a leaf, append its value to the leaf list
                leaf.append(root.val)
                return
            # Recursively explore left and right subtrees
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        # Initialize empty lists to store leaf values from both trees
        leaf1, leaf2 = [], []
        dfs(root1, leaf1)  # Collect leaf values from first tree
        dfs(root2, leaf2)  # Collect leaf values from second tree

        # Compare the sequences of leaf values from both trees
        return leaf1 == leaf2
