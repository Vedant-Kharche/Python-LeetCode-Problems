class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        Simulates asteroid collisions.
        Asteroids move in a straight line: 
        - Positive value means moving right
        - Negative value means moving left
        When two asteroids moving toward each other collide, the smaller one explodes.
        If they are equal in size, both explode.

        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []  # Stack to keep track of asteroids that are still moving

        for asteroid in asteroids:
            # While there is a collision possibility:
            # stack[-1] > 0 means last asteroid is moving right
            # asteroid < 0 means current asteroid is moving left
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    # Top asteroid is smaller in size → it explodes (pop from stack)
                    stack.pop()
                    # Continue checking for more collisions with previous asteroids
                    continue
                elif stack[-1] == -asteroid:
                    # Both asteroids are equal in size → both explode
                    stack.pop()
                # If stack[-1] > -asteroid, current asteroid explodes → break
                break
            else:
                # No collision → just push asteroid to stack
                stack.append(asteroid)

        # Return the asteroids that remain after all collisions
        return stack
