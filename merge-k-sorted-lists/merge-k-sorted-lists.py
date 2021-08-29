# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    ListNode.__eq__ = lambda self, other: self.val == other.val
    ListNode.__lt__ = lambda self, other: self.val < other.val
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.heap_sol(lists)
        
    def heap_sol(self,lists):
        h = []
        dummy = ListNode(-1)
        cur = dummy
        for p in lists:
            if p:
                heapq.heappush(h, p)
        # print(h)
        while h:
            cur.next =  heapq.heappop(h)
            cur = cur.next
            if cur and cur.next:
                heapq.heappush(h,cur.next)
        return dummy.next


    def mergeKLists_sol(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        interval= 1
        while interval < length:
            for i in range(0,length-interval,interval*2):
                print(i)
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval*=2
        return lists[0] if length>0 else None
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        
        dummy= ListNode(-1)
        ans = dummy
        while l1 and l2:
            if l1.val < l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            else:
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next
        while l1:
            ans.next = ListNode(l1.val)
            ans = ans.next
            l1 = l1.next
        while l2:
            ans.next = ListNode(l2.val)
            ans = ans.next
            l2 = l2.next
        return dummy.next