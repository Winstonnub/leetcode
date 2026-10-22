# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Idea: K way merge
        # Algorithm: Use a heap to store the first of each list, then keep popping the smallest and pushing the smallest of that list
        k = len(lists)
        if not lists:
            return None
        minHeap = [(lists[i].val, i, lists[i]) for i in range(k) if lists[i]] # (node.val, i, node)
        heapq.heapify(minHeap)
        dummy = ListNode(0, None)
        curr = dummy
        while minHeap:
            node_val, index, node = heapq.heappop(minHeap)
            if node.next:
                heapq.heappush(minHeap, (node.next.val, index, node.next))
            curr.next = node
            node.next = None
            curr = node
        return dummy.next

