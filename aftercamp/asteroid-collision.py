class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0 or (asteroid < 0 and stack[-1] < 0):
                stack.append(asteroid)
            else:
                val = asteroid
                while val < 0 and stack and stack[-1] > 0:
                    positive = stack[-1]
                    if positive < abs(val):
                        stack.pop()
                    elif positive == abs(val):
                        stack.pop()
                        val = 0
                    else:
                        val = positive
                if val < 0:
                    stack.append(val)

        return stack