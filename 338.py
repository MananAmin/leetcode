# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 1 1 2 1 2 2 3 1 2 2  3 2


class Solution:
    def main(self, n):
        if n == 0:
            return [0]
        ans = (n + 1) * [0]
        mul = 1
        for i in range(1, n + 1):
            if i == mul:
                ans[i] = 1
                mul *= 2
            else:
                ans[i] = ans[i - mul // 2] + 1
        return ans

    def compare_append(self, n):
        if n == 0:
            return [0]
        ans = [0]
        mul = 1
        for i in range(1, n + 1):
            if i == mul:
                ans.append(1)
                mul *= 2
            else:
                ans.append(ans[i - mul // 2] + 1)
        return ans


if __name__ == "__main__":
    input = 15

    print(Solution().compare_append(int(input)))
