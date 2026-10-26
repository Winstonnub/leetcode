class TrieNode:
    def __init__(self):
        self.children = {} # character, the child node
        self.isWord = False # Is this End of Word
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        # 2. Normal setup: we want a res and a visited set for our backtracking
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r,c, node, word) -> None: # current node we are at our trie, the word we have so far
            # 2.1 Is the cell r,c in range, is it already visited, and is the character of the cell possible in our current word node
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or board[r][c] not in node.children:
                return
            # 2.2 Visit cell r,c, get the node of r,c branching from our node # e.g. oa, value is t, so we branch into 'oat'
            visit.add((r,c))
            node = node.children[board[r][c]]
            # 2.3 Update the current word with newly added board[r][c]. (e.g. OA + T -> OAT). If this node is a word, add it to result
            word += board[r][c]
            if node.isWord:
                res.add(word)
            # 2.4 Now continue branch out to new words. (e.g. we are at node OAT, word OAT. Find neighbours. Looking for OATH.)
            dfs(r - 1,c,node,word)
            dfs(r + 1,c,node,word)
            dfs(r,c - 1,node,word)
            dfs(r,c + 1,node,word)
            # 2.5 Finished searching OAT, return back to OA
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "") # Root's children contains all possible starting character of the words
        return list(res)