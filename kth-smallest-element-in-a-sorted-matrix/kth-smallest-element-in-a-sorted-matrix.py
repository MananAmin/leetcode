import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return self.heap_sol(matrix,k)
    
    
    def heap_sol(self,lists,k):
        h = []
        for i,l in enumerate(lists):
            if l:
                h.append((l[0],i,0))
        heapq.heapify(h)
        cur=0
        small = 0
        while cur<k:
            cur+=1
            val,i1,i2 = heapq.heappop(h)
            small = val
            if len(lists[i1]) > i2+1:
                heapq.heappush(h,(lists[i1][i2+1],i1,i2+1))
        return small

    
    def kthSmallest_1(self, matrix: List[List[int]], k: int) -> int:
        sortlist = self.mergeKLists(matrix)
        return sortlist[k-1]    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        interval= 1
        while interval < length:
            for i in range(0,length-interval,interval*2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval*=2
        return lists[0] if length>0 else None
    
    def mergeTwoLists(self, l1, l2):
        ans = []
        ind1 = 0
        ind2 = 0
        
        while ind1<len(l1) and ind2<len(l2):
            if l1[ind1] < l2[ind2]:
                ans.append(l1[ind1])
                ind1+=1
            else:
                ans.append(l2[ind2])
                ind2+=1
                
        while ind1<len(l1):
            ans.append(l1[ind1])
            ind1+=1
            
        while ind2<len(l2):
            ans.append(l2[ind2])
            ind2+=1
            
        return ans
