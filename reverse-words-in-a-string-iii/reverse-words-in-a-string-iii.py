
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        temp = []
        for ch in s:
            if ch ==" ":
                ans.append("".join(temp))
                temp =[]
            else:
                temp.insert(0,ch)
        if temp:
            ans.append("".join(temp))
        return " ".join(ans)