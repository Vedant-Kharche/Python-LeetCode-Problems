class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # Depth-First Search to explore all nodes (cities) in a province
        def dfs(i): 
            self.visited.add(i)  # Mark the current city as visited
            for j in range(n):   # Check all possible cities
                # If city j is connected to city i and not yet visited
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)  # Visit city j
            return  # Optional, for clarity

        province = 0  # This will count the number of provinces
        self.visited = set()  # Track visited cities
        n = len(isConnected)  # Total number of cities

        for i in range(n):  # Loop through each city
            if i not in self.visited:  # If city not visited, it's a new province
                province += 1  # Increment province count
                dfs(i)  # Explore all cities in this province using DFS
        
        return province  # Return the total number of provinces
