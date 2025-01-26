#best solutionn on stack
def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
#my solution
def asteroidCollision(self, asteroids):
        stack=[]
        count=0
        for j in range(len(asteroids)):
            if asteroids[j]<0:
                count+=1
        if count == len(asteroids):
            return asteroids
        else:
            for i in range(len(asteroids)):
                if asteroids[i] > 0:
                    stack.append(asteroids[i])
                elif abs(asteroids[i-1]) <= abs(asteroids[i]):
                    stack.pop()
            

        return stack