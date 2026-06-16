class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums :
            if num in visited and visited[num] > 0 : 
                return True
            visited[num] = visited.get(num,0) + 1
        return False