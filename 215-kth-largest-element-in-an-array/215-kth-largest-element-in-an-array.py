import random
from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pq = PriorityQueue() 
        
        for num in nums:
            pq.put(-1*num)
        
        ans = nums[0]
        for i in range(k):
            ans = pq.get()
            
        return ans*-1
            
        