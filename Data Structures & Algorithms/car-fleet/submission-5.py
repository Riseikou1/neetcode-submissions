class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        temuujin = sorted([(p,(target-p)/s) for p,s in zip(position,speed)],reverse=True)

        stack = []

        for _,time in temuujin :
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)