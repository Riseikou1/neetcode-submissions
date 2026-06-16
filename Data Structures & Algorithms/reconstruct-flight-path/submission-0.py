class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        res = []

        for src, dst in reversed(sorted(tickets)) :
            graph[src].append(dst)

        def dfs(city) :
            while graph[city] :
                dfs(graph[city].pop())
            res.append(city)

        dfs('JFK')
        return res[::-1]
