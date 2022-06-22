import random
from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.another(nums,k)
    
    def another(self,nums,k):
        
        pq = PriorityQueue()
        
        for index,num in enumerate(nums):
            if index <k:
                pq.put(num)
            else:
                pq.put(num)
                pq.get()     
        return pq.get()
    
    def naive(self,nums,k):
        pq = PriorityQueue() 
        
        for num in nums:
            pq.put(-1*num)
        
        ans = nums[0]
        for i in range(k):
            ans = pq.get()
            
        return ans*-1
    
    def heap_sol(self,nums,k):
        pq = nums[:k]
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x)
            heapq.heappop(pq)
        return pq[0]
        