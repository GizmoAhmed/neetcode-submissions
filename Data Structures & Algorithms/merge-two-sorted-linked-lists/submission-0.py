# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c3 = list3 = ListNode()
        c1 = list1
        c2 = list2
        while True:
            if c1 is None and c2 is None:
                return list3.next

            if c1 is not None and (c2 is None or c1.val <= c2.val):
                print(str(c1.val) + " is less than " + (str(c2.val) if c2 else "None"))
                c3.next = ListNode(c1.val)
                c1 = c1.next
            elif c2 is not None:
                print(str(c2.val) + " is less than " + (str(c1.val) if c1 else "None"))
                c3.next = ListNode(c2.val)
                c2 = c2.next

            c3 = c3.next
