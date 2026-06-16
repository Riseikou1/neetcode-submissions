class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList : return 0
        visited = set([beginWord])
        q = deque([(beginWord)])
        count = 1
        temuujin = defaultdict(list)

        for word in wordList :
            for idx in range(len(word)) :
                pattern = word[:idx] + '*' + word[idx + 1 :]
                temuujin[pattern].append(word)

        while q :
            for _ in range(len(q)) :
                curWord = q.popleft()
                if curWord == endWord :
                    return count 
                for i in range(len(curWord)) :
                    pattern = curWord[:i] + '*' + curWord[i + 1 :]
                    for nei in temuujin[pattern] :
                        if not nei in visited :
                            visited.add(nei)
                            q.append(nei)
            count += 1

        return 0