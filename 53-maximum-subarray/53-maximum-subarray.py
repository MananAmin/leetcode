class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur  = 0
        for num in nums:
            cur+=num
            ans = max(cur,ans)
            if cur < 0:
                cur=0
        return ans