class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temuujin = []
        stack = []

        temuujin = [(position[i], speed[i]) for i in range(len(speed))]

        temuujin.sort()  # Ascending by position

        for i in range(len(temuujin) - 1, -1, -1):  # 🔧 fix: include index 0
            stack.append(temuujin[i])

            if len(stack) > 1:
                # 🔧 fix: compare the last two cars that are in the stack
                time1 = (target - stack[-2][0]) / stack[-2][1]
                time2 = (target - stack[-1][0]) / stack[-1][1]
                
                if time1 >= time2:
                    stack.pop()  # remove the later one, since it merges

        return len(stack)
