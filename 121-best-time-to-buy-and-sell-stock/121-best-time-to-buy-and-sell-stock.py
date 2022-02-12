class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)==1:
            return 0
        
        return self.best(prices)
    
    def best(self,prices):
        ans = 0
        size = len(prices)
        left =0
        right =1
        
        while right<size:
            
            if prices[right]<prices[left]:
                left = right
            elif prices[right]-prices[left]>ans:
                ans = prices[right]-prices[left]
                right+=1
            else:
                right+=1
        return ans
    
    def solution(self,prices):
        ans = 0
        size = len(prices)
        left =0
        right =1
        
        while left< size and right<size:
            
            if prices[right]<prices[left]:
                left+=1
            elif prices[right]-prices[left]>ans:
                ans = prices[right]-prices[left]
                right+=1
            else:
                right+=1
        return ans
        
    def sol1(self,prices):
        
        ans = 0
        for i in range(len(prices)):
            
            for j in range (i+1,len(prices)):
                
                if prices[j]-prices[i]>ans:
                    ans = prices[j]-prices[i]
        return ans
    