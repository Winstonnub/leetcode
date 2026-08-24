# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        # 1. Use dummy to avoid inserting into empty list
        # 2. while there are stuff in list1 or list2
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # 3. append the remaining list to the list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
