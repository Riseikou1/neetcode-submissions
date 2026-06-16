class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, seen) :
            if len(cur) == len(nums) :
                res.append(list(cur)) 
                return 

            for i in range(len(nums)) :
                if not i in seen :
                    seen.add(i)
                    cur.append(nums[i])

                    dfs(cur, seen)

                    cur.pop()
                    seen.remove(i)

        dfs([],set())
        return res