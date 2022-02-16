class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return self.solution(nums)
    
    def solution(self,nums):
        
        flag = set()
        
        for i in nums:
            if i in flag:
                return True
            flag.add(i)
        return False
        