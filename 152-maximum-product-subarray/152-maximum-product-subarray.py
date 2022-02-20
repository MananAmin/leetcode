class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        return self.dp_sol(nums)
    
    def dp_sol(self,nums):
        
        ans = nums[0]
        curMin = 1
        curMax = 1
        for num in nums:
            if num==0:
                curMin =1
                curMax =1
                ans = max(0,ans)
            else:
                temp = curMax
                curMax = max(num,num*curMin,curMax*num)
                curMin = min(num,num*temp,num*curMin)
                ans = max(ans,curMax)
        return ans
        
    def first_sol(self,nums):
        left =0
        right = 0
        cur = 1
        ans = nums[0]
        while right<len(nums):
            if nums[right]==0:
                while left < right-1:
                    if nums[left]!=0:
                        cur/=nums[left]
                        ans = max(ans,cur)
                    left+=1
                cur=1
                left= right+1
                ans = max(0,ans)
            else:
                cur *=nums[right]
                ans = max(ans,cur)
            right+=1
        
        while left < right-1:
            if nums[left]!=0:
                cur /=nums[left]
                ans = max(ans,cur)
            left+=1
            
        return int(ans)
            
            
            