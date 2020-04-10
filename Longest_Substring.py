# 3. Longest Substring Without Repeating Characters

# link https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        ans = -1

        for end, ch in enumerate(s):

            if ch in dic:
                temp = dic[ch] + 1
                if temp > start:
                    start = temp

            dic[ch] = end

            if end - start > ans:
                ans = end - start

        return ans + 1


if __name__ == "__main__":
    try:
        sol = Solution()
        ans = sol.lengthOfLongestSubstring("abcabcbb")
        if int(ans) == 3:
            print(True)
        else:
            print(False)
    except Exception as e:
        print(e)
