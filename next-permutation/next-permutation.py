class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sol(nums)
    
    
#     6 2 5 4 2 1 ->  
    def sol(self,nums):
        
        cur = len(nums) -1
        while cur>0 and nums[cur-1] >= nums[cur]:
            cur-=1
        swap = cur-1
        if cur==0:
            self.reverse(nums,0)
        else:
            cur =len(nums) -1
            while cur>0 and nums[cur] <= nums[swap]:
                cur-=1
            nums[cur],nums[swap] = nums[swap], nums[cur]
            self.reverse(nums,swap+1)
    
    def reverse(self,nums,start):
        end = len(nums) -1
        while start<end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        
        