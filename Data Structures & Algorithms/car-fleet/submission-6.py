class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, (target - p) / s) for p, s in zip(position, speed)], reverse=True)

        fleets = 0
        cur_time = 0

        for pos, time in cars:
            if time > cur_time:
                fleets += 1
                cur_time = time

        return fleets
