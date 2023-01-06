import math


class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0

        while l <= r:
            if count > math.log2(len(nums)) + 2:
                return -1
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


if __name__ == "__main__":
    input = [1]
    target = 1

    print(Solution().search(input, target))
