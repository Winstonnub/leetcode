class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    
    # dummy left and right node makes insert / remove logic cleaner
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # make a hashmap
        # Create doubly linked list
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node): # Just unlink from the doubly linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # remove if need update
        self.cache[key] = Node(key, value) # create the node in hashmap
        self.insert(self.cache[key]) # insert into the doubly linked list

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru) # Unlink from the doubly linked list
            del self.cache[lru.key] # remove from hash map
         
