class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        visited = set(beginWord)
        wordSet = set(wordList)
        q = deque([]) # BFS length: we are at number of words = 1
        q.append((beginWord, 1))
        while q:
            node, steps = q.popleft()
            if node == endWord:
                return steps
            # Generate all possible
            neighbours = []
            for i in range(len(node)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = node[:i] + c + node[i+1:]
                    neighbours.append(new_word)
            for nei in neighbours:
                if nei in wordSet and nei not in visited:
                    q.append((nei, steps + 1))
                    visited.add(nei)
        return 0

            