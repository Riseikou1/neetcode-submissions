class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if r - q[0] >= k:
                q.popleft()

            if r >= k -1 :
                output.append(nums[q[0]])

        return output
