class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, skip = 0, 0
        
        for num in nums :
            tmp = skip   # save old skip value from prev steps.
            skip = max(skip, rob + num)  # skipping or robbing this house is up to us.
            rob = tmp  #  change it for the next iteration.
                       # cos current skip will be potential rob for the next houses.

        return skip