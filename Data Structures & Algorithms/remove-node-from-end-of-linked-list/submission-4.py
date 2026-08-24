# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Strategy: find the length, then use prev next
        curr = head
        l = 0
        while curr != None:
            curr = curr.next
            l += 1
        # Length l is 3 for [0,1,2]
        # To remove 1, 3-2 = 1 (index 1)
        i = l - n
        prev, curr = ListNode(), head
        newhead = prev
        newhead.next = head
        if i == 0 and l == 1:
            return None
        while curr != None:
            if i == 0:
                prev.next = curr.next
                break
            prev, curr = curr, curr.next
            i -= 1
        return newhead.next
