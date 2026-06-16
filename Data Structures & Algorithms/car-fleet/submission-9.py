class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if a car catches a car ahead of it before reaching the destination, pop it.
        # if it can't, then it will be an independent fleet.
        # return len of lst
        fleet = []
        for i in range(len(position)) :
            fleet.append((position[i], speed[i]))
        fleet.sort()
        res = [fleet[-1]]
        for i in range(len(fleet) - 2, -1, -1) :
            time1 = (target - res[-1][0]) / res[-1][1]
            time2 = (target - fleet[i][0]) / fleet[i][1]
            if time2 > time1 :
                res.append(fleet[i])

        return len(res)
