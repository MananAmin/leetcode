class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
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
