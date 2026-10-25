# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # 1. 
        dummy = ListNode(0, head)
        group_prev = dummy # The previous node from group 1, 2, 3 is dummy. Similarly, 4, 5, 6's previous would be 1 after reverse.
        while True:
            # 1. Find kth, the kth node (end of our group)
            kth = group_prev
            for _ in range(k): # from dummy to 1 to 2 to 3
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            # Now kth is the last node in our 1,2,3 group, (kth = 3)
            # group_next = 4

            # 2. Reverse the group
            # Point 1 to 4 first (The current group_head to the next group's head)
            prev, curr = group_next, group_prev.next # 4 and 1
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt
            # Now curr = 4, prev = 3

            # 3. Stitch
            old_start = group_prev.next # dummy's next is 1
            group_prev.next = prev # dummy's next equal to 3 now
            group_prev = old_start # now the node before the new group (4) is 1
            
            

        
