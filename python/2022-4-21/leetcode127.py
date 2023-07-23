import collections


class Solution(object):
    def check(self, first, second):
        """
        :type first: str
        :type second: str
        :return: bool
        """
        """
        n = len(first)
        count = 0
        for i in range(n):
            if first[i] == second[i]:
                continue
            else:
                count += 1
        if count == 1:
            return True
        else:
            return False
        """

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type
        beginWord: str
        :type
        endWord: str
        :type
        wordList: List[str]
        :rtype: int
        """
        """
        words = {}
        index = 0
        begin_index = -1
        for word in wordList:
            if word == beginWord:
                begin_index = index
            words[word] = index
            index += 1
        if -1 == begin_index:
            words[beginWord] = index
            begin_index = index
            index += 1
        n = index

        q = []
        visited = [False] * n
        step = [0] * n
        step[begin_index] = 1
        q.append(beginWord)
        visited[begin_index] = True
        while len(q) > 0:
            current = q.pop(0)
            if current == endWord:
                return step[words[current]]
            for word, i in words.items():
                if word == current:
                    continue
                if self.check(word, current) and not visited[i]:
                    q.append(word)
                    step[i] = step[words[current]] + 1
                    visited[i] = True

        return 0
        """
        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        def addWord(word):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                temp = chars[i]
                chars[i] = '*'
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = temp

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        disBegin = [float('inf')] * nodeNum
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = collections.deque([beginId])

        disEnd = [float('inf')] * nodeNum
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = collections.deque([endId])

        while queBegin or queEnd:
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != float('inf'):
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float('inf'):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)

            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != float('inf'):
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == float('inf'):
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)

        return 0


s = Solution()
print(s.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(s.ladderLength('a', 'c', ['a', 'b', 'c']))
