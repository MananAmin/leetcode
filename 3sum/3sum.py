class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.three_sum(nums)
        
    def three_sum(self,nums):
        nums.sort()
        ans = []
        
        for i,value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
                
            left = i+1
            right = len(nums)-1
            
            while left < right:
                threesum = value + nums[left] + nums[right]
                if threesum > 0:
                    right-=1
                elif threesum <0:
                    left+=1
                else:
                    ans.append([value, nums[left] , nums[right]])
                    left+=1
                    while nums[left] ==nums[left-1] and left<right:
                        left+=1
        return ans