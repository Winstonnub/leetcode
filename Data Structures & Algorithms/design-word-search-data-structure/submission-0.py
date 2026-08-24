class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr.children:
                if c == '.':
                    res = False
                    new = WordDictionary()
                    new.root = curr
                    for d in "abcdefghijklmnopqrstuvwxyz":
                        if new.search(d + word[i+1:]) == True:
                            return True
                return False
            curr = curr.children[c]
        return curr.endOfWord
        

        
