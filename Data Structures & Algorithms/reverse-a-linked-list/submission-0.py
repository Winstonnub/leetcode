# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

  

# At 0: we store 1's next (2), then point 1 to itself
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next_pointer = curr.next
            curr.next = prev
            prev = curr 
            curr = next_pointer
        head = prev
        return head

            
