class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)<3:
            return min(nums)
        return self.first_attempt(nums)
        
    
    def first_attempt(self,nums):
        small = nums[0]
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            print(left,"l  ",right,"r ",mid)
            
            
            if nums[mid] >= nums[0]:
                left=mid+1
            else:
                if nums[mid]<small:
                    small=nums[mid]
                right = mid-1
        return small