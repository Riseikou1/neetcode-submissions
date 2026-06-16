class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        count = defaultdict(set)
        unique_chars = set("".join(words))

        for word1, word2 in zip(words[:-1], words[1:]) :
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen] :
                return ""
            for j in range(minLen) :
                if word1[j] != word2[j] :
                    count[word1[j]].add(word2[j])
                    break

        visited = {}  # False => visited, True => visited & current path
        res = []

        def dfs(c) :
            if c in visited :
                return visited[c]
            visited[c] = True

            for nei in count[c] :
                if dfs(nei) :
                    return True

            visited[c] = False
            res.append(c)

        for c in unique_chars :
            if dfs(c) :
                return ""

        return "".join(reversed(res))


