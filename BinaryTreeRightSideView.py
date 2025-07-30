class Solution(object):
    def rightSideView(self, root):
        res = []  # This will store the final right side view

        # Initialize queue with the root node for BFS
        q = collections.deque([root])

        # Perform level-order traversal
        while q:
            rightside = None  # To keep track of the last non-null node at current level
            qlen = len(q)  # Number of nodes at current level

            for i in range(qlen):
                node = q.popleft()  # Pop the node from front of the queue
                if node:
                    rightside = node  # Update the last seen node at this level
                    q.append(node.left)   # Add left child to queue for next level
                    q.append(node.right)  # Add right child to queue for next level

            # After traversing the level, if there was any valid node, add its value to result
            if rightside:
                res.append(rightside.val)

        return res