# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 1 1 2 1 2 2 3 1 2 2  3 2


class Solution:
    def main(self, n):
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans


if __name__ == "__main__":
    input = 11

    print(Solution().main(int(input)))
