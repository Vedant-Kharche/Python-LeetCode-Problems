class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a mapping from each course to its list of prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # A set to keep track of courses in the current DFS path
        visitSet = set()

        # Helper function to perform DFS and check for cycles
        def dfs(crs):
            # If the course is already in the current DFS path, we have a cycle
            if crs in visitSet:
                return False  # cannot finish due to cycle

            # If the course has no prerequisites left, it's safe to take
            if preMap[crs] == []:
                return True

            # Add course to the current path
            visitSet.add(crs)
            
            # Recursively check all prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False  # cycle detected in prerequisites
            
            # Remove course from current path after exploring
            visitSet.remove(crs)

            # Mark course as completed by clearing prerequisites
            preMap[crs] = []

            return True  # this course can be finished

        # Check each course to see if it can be completed
        for crs in range(numCourses):
            if not dfs(crs):
                return False  # found a cycle, cannot finish all courses

        return True  # all courses can be finished
