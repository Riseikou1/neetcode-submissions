class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in reversed(sorted(tickets)) :
            graph[src].append(dst)

        stack = ['JFK']
        res = []

        while stack :
            cur = stack[-1]
            if not graph[cur] :
                res.append(stack.pop())
            else :
                stack.append(graph[cur].pop())

        return res[::-1]