# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.first_sol(head)
    
    def first_sol(self,head):
        
        dummy = cur = ListNode(-1)
        cur.next =head        
        while cur.next and cur.next.next:
            temp = cur.next
            nex = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = temp
            cur = cur.next.next
            cur.next = nex
        
        return dummy.next
        
            
        
        
        