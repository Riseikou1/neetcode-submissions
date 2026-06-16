class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        l = r = 0
        q = deque()

        while r < len(nums):

            while q and nums[r] > nums[q[-1]] :
                q.pop()
            q.append(r)

            if q[0] < l :
                q.popleft()

            if r >= k - 1 :
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output