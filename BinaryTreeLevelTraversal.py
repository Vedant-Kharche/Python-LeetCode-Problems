# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # This will store the final result: a list of lists, where each inner list contains nodes at the same level

        # Use a deque for efficient popping from the left
        q = collections.deque()
        q.append(root)  # Start BFS with the root node

        # Continue BFS until there are no more nodes to process
        while q:
            qLen = len(q)  # Number of nodes at the current level
            level = []     # List to store values of nodes at the current level

            # Process all nodes at the current level
            for i in range(qLen):
                node = q.popleft()  # Remove the node from the queue
                if node:
                    level.append(node.val)  # Add the node's value to the current level list
                    # Add left and right children to the queue for the next level
                    q.append(node.left)
                    q.append(node.right)

            # Only add the level to result if it has any node values
            if level:
                res.append(level)

        return res  # Return the final list of levels
