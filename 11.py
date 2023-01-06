class Solution:
    def main(self, nums):
        ans = 0
        l, r, d = 0, len(nums) - 1, len(nums) - 1

        while l < r:
            ans = max(ans, min(nums[l], nums[r]) * d)
            if nums[l] <= nums[r]:
                l += 1
            else:
                r -= 1
            d -= 1
        return ans


if __name__ == "__main__":
    input = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(Solution().main(input))
