class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        matchMap = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                matchMap[pattern].append(w)
        seen = set([beginWord])
        q = collections.deque([beginWord])
        r = 1
        while q:
            for i in range(len(q)):
                checkWord = q.popleft()
                if checkWord == endWord:
                    return r
                for j in range(len(checkWord)):
                    pat = checkWord[:j] + "*" + checkWord[j+1:]
                    for word in matchMap[pat]:
                        if word not in seen:
                            q.append(word)
                            seen.add(word)
            r += 1
        return 0
