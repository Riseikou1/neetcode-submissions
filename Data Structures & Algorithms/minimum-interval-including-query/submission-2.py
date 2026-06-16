class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        indexed_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        min_heap = []
        res = [0] * len(queries)
        i = 0

        for val, idx in indexed_queries :
            while i < len(intervals) and val >= intervals[i][0] :
                dist = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(min_heap, (dist, intervals[i][1]))
                i += 1

            while min_heap and min_heap[0][1] < val :
                heapq.heappop(min_heap)

            res[idx] = min_heap[0][0] if min_heap else -1

        return res

