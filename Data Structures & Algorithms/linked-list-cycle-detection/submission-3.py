# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        i = ListNode()
        j = ListNode()

        i = head
        j = i.next

        if i.next == None: # one-node list
            return False

        while True:
            if j.next == None or i.next == None:
                return False
            j = j.next.next
            i = i.next
            if i == j:
                return True
        
        return False
        