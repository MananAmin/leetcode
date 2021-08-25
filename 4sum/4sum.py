class Solution:
    def fourSum(self, nums, target: int):
        results = []
        self.nsum(sorted(nums),4, target,[], results)
        return results
    
    def nsum(self,nums,n,target,partial,results):
        # print(nums,n,target,partial,results)
        # added this condition for early return, saw it in editorial lol
        if len(nums)<n or nums[-1]*n <target or nums[0]*n > target:
            return
        if n==2:
            left = 0
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(partial + [nums[left],nums[right]])
                    right-=1
                    left+=1
                    while left < right and nums[right] ==nums[right+1]:
                        right-=1
                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    left+=1
        elif n>2:
            for i in range(len(nums)-n+1):
                if i > 0 and nums[i] ==nums[i-1]:
                    continue
                self.nsum(nums[i+1:],n-1, target-nums[i],partial+[nums[i]], results)