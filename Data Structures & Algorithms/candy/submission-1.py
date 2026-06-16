class Solution:
    def candy(self, ratings: List[int]) -> int:
        min_heap = []
        dp = [1] * len(ratings)
        if len(ratings) == 1 : 
            return 1

        for idx, num in enumerate(ratings) :
            heapq.heappush(min_heap, [num, idx])

        while min_heap :
            cur, idx = heapq.heappop(min_heap)
            if idx == 0 :
                if ratings[idx + 1] < cur :
                    dp[idx] = dp[idx + 1] + 1

            elif idx == len(ratings) - 1 :
                if ratings[idx - 1] < cur :
                    dp[idx] = dp[idx - 1] + 1

            else :
                if ratings[idx + 1] < cur :
                    dp[idx] = max(dp[idx], dp[idx + 1] + 1)

                if ratings[idx - 1] < cur :
                    dp[idx] = max(dp[idx], dp[idx - 1] + 1)

        return sum(dp)
