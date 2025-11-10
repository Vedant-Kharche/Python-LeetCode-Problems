"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to map each original node to its cloned copy
        oldToNew = {}

        def dfs(node):
            # ✅ If we've already cloned this node, return its copy
            if node in oldToNew:
                return oldToNew[node]

            # 🔹 Create a new copy of the current node (no neighbors yet)
            copy = Node(node.val)
            # Save mapping: original node -> cloned node
            oldToNew[node] = copy

            # 🔁 Recursively clone all neighbors
            for nei in node.neighbors:
                # Append the cloned neighbor to this node's neighbor list
                copy.neighbors.append(dfs(nei))

            return copy

        # Start DFS from the given node if it's not None
        return dfs(node) if node else None
