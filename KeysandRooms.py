class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        Determines if all rooms can be visited starting from room 0.

        :type rooms: List[List[int]]  # rooms[i] contains keys for other rooms
        :rtype: bool  # Returns True if all rooms can be visited, False otherwise
        """
        # Set to track which rooms we've already visited
        visited = set()
        
        # Stack to simulate DFS traversal; start from room 0
        stack = [0]

        # Continue while there are rooms to visit
        while stack:
            # Get the current room from the top of the stack
            room = stack.pop()
            
            # Mark the room as visited
            visited.add(room)

            # Loop through all keys (i.e., other rooms) available in this room
            for key in rooms[room]:
                # If we haven't visited the room corresponding to the key, add it to stack
                if key not in visited:
                    stack.append(key)
        
        # If number of visited rooms equals total rooms, return True
        return len(visited) == len(rooms)
