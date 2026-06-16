class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets :
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2] :
                continue
                
            for idx, num in enumerate(t) :
                if num == target[idx] :
                    good.add(idx)
                    if len(good) == 3 : return True

        return len(good) == 3