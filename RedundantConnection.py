class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Number of edges (same as number of nodes, since there's one extra edge forming a cycle)
        n = len(edges)
        
        # Create adjacency list for an undirected graph
        adj = [[] for _ in range(n + 1)]

        # Depth-First Search (DFS) to check if adding an edge creates a cycle
        def dfs(node, par):
            # If this node is already visited, a cycle is detected
            if visit[node]:
                return True

            # Mark current node as visited
            visit[node] = True

            # Traverse all neighbors
            for nei in adj[node]:
                # Skip the edge leading back to the parent node
                if nei == par:
                    continue

                # If a recursive call finds a cycle, return True
                if dfs(nei, node):
                    return True

            # No cycle found through this path
            return False

        # Try adding each edge one by one
        for u, v in edges:
            # Add the edge to adjacency list
            adj[u].append(v)
            adj[v].append(u)

            # Track visited nodes for the current DFS check
            visit = [False] * (n + 1)

            # If a cycle is formed by adding this edge, it’s the redundant one
            if dfs(u, -1):
                return [u, v]

        # If no redundant edge found (shouldn’t happen per problem constraints)
        return []
