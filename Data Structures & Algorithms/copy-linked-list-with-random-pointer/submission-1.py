"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Notes
# We want to make a deep copy.
# Each copied node needs: value, the next node, and the new random node.

# My algorithm:
# 1. Loop through each original node. Create a copy of that node. Store the copy in a hashmap with the original node as the key. Link the last node's next to this node.
# 2. Loop through each original node again. At each node, we check the random node. Then we use hashmap to link the deep copy node to the random node.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None} # We cannot just use dict()! How about a None key?
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

        