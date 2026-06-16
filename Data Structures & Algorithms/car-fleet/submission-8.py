class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)) :
            position[i] = [position[i], i]

        for pos,idx in reversed(sorted(position)) :
            time = (target - pos) / speed[idx]
            if not stack or stack[-1] < time :
                stack.append(time)

        return len(stack)
