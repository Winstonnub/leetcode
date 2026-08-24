# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Two pointers
        [1,2,3,4,5]
        # Keep head
        # traverse to find the end of the list
        # while head is not tail, we keep append step by step
        # Step 1: Use slow fast pointer to find the second half
        # Step 2: Reverse the second half
        # Step 3: Merge the array
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Now fast reaches end, so slow is in middle. 
        # The second part starts at slow.next
        # We chop the linked list into two
        second = slow.next
        slow.next = None 
        # Reverse [3,4,5] using the prev, curr structure with tmp (nextpointer)
        prev = None
        while second:
            next_pointer = second.next
            second.next = prev
            prev = second
            second = next_pointer
        # So now prev contains 5, the 'start' of this new list
        # 3. Merge the array
        first, second = head, prev
        while second:
            # Since we will break two chains, we store them
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

    