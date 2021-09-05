class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        if k >1:
            return "".join(sorted(s))
        else:
            ans = s
            for i in range(len(s)):
                if s[i:] + s[:i] < ans:
                    ans =  s[i:] + s[:i] 
            return ans