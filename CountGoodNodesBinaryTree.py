class Solution(object):
    def goodNodes(self, root):
    
        # function to perform DFS traversal and count good nodes
        def dfs(node, maxVal):
            if not node:
                return 0  # Base case: if the node is None, return 0

            # If the current node's value is greater than or equal to the max value
            # seen so far on the path, it is a "good" node
            res = 1 if node.val >= maxVal else 0

            # Update the max value seen so far on this path
            maxVal = max(node.val, maxVal)

            # Continue DFS traversal for left and right children
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val)
