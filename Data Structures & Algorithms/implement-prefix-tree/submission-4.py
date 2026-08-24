class TrieNode:
    # children are stored in hashmap
    # store if this node is end of a word
    def __init__(self):
        self.children = dict()
        self.endOfWord = False # not a word yet


class PrefixTree:
    #Trie
    # We need
    # 1. PrefixTree is a TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # insert 'apple'
        # Remember we start cur at the root of the node
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True



    def search(self, word: str) -> bool:
        # search 'apple'
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # search 'app'
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        