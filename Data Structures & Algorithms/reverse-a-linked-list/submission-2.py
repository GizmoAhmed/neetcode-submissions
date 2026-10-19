# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        c = ListNode()
        n = ListNode()
        p = ListNode()

        c = head
        n = head.next

        if n == None:
            return c

        while True:
            if c == head:
                c.next = None
                p = n.next
                n.next = c
                c = p
                if c == None:
                    return n
                p = n
                n = c.next
            else:
                c.next = p
                p = c
                c = n
                n = c.next
            
            if n == None:
                c.next = p
                return c
                
                
                

            

            




        