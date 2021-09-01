# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.first_sol(head)
    
#  1 -> 2 -> 3
#  
    def first_sol(self,head):
        pre , cur, nex =None , head,None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
        
        