class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        return self.boolarray_sol(nums)
    
    def first_sol(self,nums):
        ans = 0
        visited = set()
        for i in range(len(nums)):
            if i in visited:
                continue
            else:
                temp = 1
                visited.add(i)
                cur = nums[i]
                while cur !=i:
                    cur = nums[cur]
                    temp+=1
                    visited.add(cur)
                if temp > ans:
                    ans =temp
        return ans
    
    def boolarray_sol(self,nums):
        ans = 0
        visited = [False]*len(nums)
        for i in range(len(nums)):
            if visited[i]:
                continue
            else:
                temp = 1
                visited[i] = True
                cur = nums[i]
                while cur !=i:
                    cur = nums[cur]
                    temp+=1
                    visited[cur] = True
                ans =max(ans,temp)
        return ans