# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count+=1
        if count<k:
            return head
        new_head, prev = self.reverse_ll(head,k)
        head.next = self.reverseKGroup(new_head,k)
        return prev
        
#     1 -> 2 -> 3 ->next ===>  (prev) 3 -> 2 ->  1 ->next(cur)
    def reverse_ll(self,head,count):
        prev,cur = None,head
        while count>0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            count-=1
        return (cur,prev)
            