class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        return self.sol(nums)
    
    
    def sol(self,nums):
        ans = []
        le = len(nums)
        ans.append(1)
        pre = 1
        for i in range(1,le):
            pre *=nums[i-1]
            ans.append(pre)
        
        su =1
        for i in range(1,le):
            su*=nums[le-i]
            ans[le-i-1] = ans[le-i-1]*su
        
        return ans
        