class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Quick check: a tree with n nodes must have exactly n-1 edges.
        # If edges count differs, it can't be a tree (either disconnected or has extra cycles).
        if n == 0:
            # By convention: an empty graph can be considered a valid tree. If your platform
            # requires False for n==0, change this accordingly.
            return True
        if len(edges) != n - 1:
            return False

        # Build adjacency list for the undirected graph
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            """
            Return False if a cycle is detected reachable from `node`, True otherwise.
            parent is the node we came from so we don't treat the immediate back-edge as a cycle.
            """
            # mark current node visited
            visited.add(node)

            # iterate neighbors
            for nei in adj[node]:
                # skip the parent node (the edge back to parent is not a cycle)
                if nei == parent:
                    continue

                # if neighbor already visited, we found a cycle
                if nei in visited:
                    return False

                # recursively visit neighbor; if subtree has a cycle, propagate False
                if not dfs(nei, node):
                    return False

            # no cycle found in this branch
            return True

        # Start DFS from node 0 (any node could be used).
        # If DFS returns True (no cycle) AND we've visited all nodes (connected), it's a tree.
        return dfs(0, -1) and len(visited) == n
