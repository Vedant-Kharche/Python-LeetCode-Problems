class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # ✅ A tree with n nodes must have exactly (n-1) edges
        # If there are more than n-1 edges, it MUST contain a cycle → not a tree
        if len(edges) > (n - 1):
            return False

        # ✅ Build adjacency list for the undirected graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # ✅ Keep track of visited nodes
        visit = set()

        # ✅ Depth First Search (DFS) to detect cycles and traverse graph
        def dfs(node, par):
            # If we revisit a node, that means we found a cycle → not a tree
            if node in visit:
                return False

            visit.add(node)

            # Explore all neighbors
            for nei in adj[node]:
                # Skip the parent (don't go back where we came from)
                if nei == par:
                    continue
                # If DFS on neighbor returns False, graph is not a tree
                if not dfs(nei, node):
                    return False
            return True

        # ✅ A valid tree must satisfy two conditions:
        # 1. Connected → all nodes must be visited (len(visit) == n)
        # 2. No cycles → DFS must return True
        return dfs(0, -1) and len(visit) == n
