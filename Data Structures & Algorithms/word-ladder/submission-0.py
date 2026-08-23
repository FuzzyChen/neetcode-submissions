class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def isAdj(w1,w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff == 1
        
        fullList = [beginWord] + wordList
        adj = {word:[] for word in fullList}

        for i in range(len(fullList)):
            for j in range(i,len(fullList)):
                if isAdj(fullList[i],fullList[j]):
                    adj[fullList[i]].append(fullList[j])
                    adj[fullList[j]].append(fullList[i])
        q = deque([beginWord])
        visited = {beginWord}
        res = 1

        while q:
            for _ in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return res
                for nei in adj[curWord]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            res += 1
        return 0

