# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        r = 0
        A = l1
        B = l2
        C = ListNode()
        final = C   # Keep head reference

        while A or B or r > 0:
            s = (A.val if A else 0) + (B.val if B else 0) + r
            C.val = s % 10
            r = s // 10

            A = A.next if A else None
            B = B.next if B else None

            if A or B or r > 0:
                C.next = ListNode()
                C = C.next

        return final


        