class Solution:
    # x + y + z= 0
    def duplicate_main(self, nums):
        ans = []
        for x in nums:
            values = set()
            for y in nums:
                if -1 * (x + y) in values:
                    ans.append([x, y, -1 * (x + y)])
                else:
                    values.add(y)
        return ans

    def main(self, nums):
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i - 1] == num:
                continue
            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[i], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans


if __name__ == "__main__":
    input = [-2, -2, 0, 0, 2, 2]

    print(Solution().main(input))
