class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temuujin = sorted([(p,(target-p)/s) for p,s in zip(position,speed)],reverse=True)
        fleets = 1
        prevTime= temuujin[0][1]

        for _,time in temuujin[1:] :
            if time > prevTime :
                fleets += 1
                prevTime = time
        return fleets