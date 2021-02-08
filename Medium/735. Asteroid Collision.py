class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for asteroid in asteroids:
            if len(stack) == 0 or asteroid > 0:
                stack.append(asteroid)
            else:
                while len(stack) > 0 and stack[-1] > 0 and asteroid < 0: 
                    top = stack.pop()
                    if abs(top) == abs(asteroid):
                        break
                    elif abs(top) > abs(asteroid):
                        stack.append(top)
                        break
                    elif abs(top) < abs(asteroid):
                        continue
                else:
                    stack.append(asteroid)
                
        return stack