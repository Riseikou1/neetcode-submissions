class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)
        res = []

        for i in range(len(s)) :
            count[s[i]] = max(count.get(s[i], float('-inf')), i)

        i = 0
        while i < len(s) :
            size = 1
            end = count[s[i]]
            while i < end :
                i += 1
                end = max(end, count[s[i]])
                size += 1

            i += 1
            res.append(size)

        return res