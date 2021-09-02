class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.o1_sol(s)
        
        
    def dp_sol(self,s):
        
        dp = [0]*len(s)
        ans =0
        for i in range(1,len(s)):
            
            if s[i] ==")":
                if s[i-1] =="(":
                    dp[i] = dp[i-2]+2 if i >= 2 else 2
                else:
                    if i - dp[i-1] -1 >= 0 and  s[i - dp[i-1] -1]=="(":
                        dp[i] = dp[i-1]+ 2 + ( dp[i - dp[i-1] -1] if i - dp[i-1] -1 >=2 else 0) 
            # print(dp[i])
            ans = max(ans,dp[i])
        return ans
                
    
    def stack_sol(self,s):
        
        stack = []
        ans =0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] =="(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(ans,i-stack[-1])
                else:
                    stack.append(i)
        return ans
    
    def o1_sol(self,s):
        ans =0
        left =0
        right =0
        for c in s:
            if c=="(":
                left+=1
            else:
                right+=1
                
            if left==right:
                ans = max(ans,left*2)

            if right > left:
                left=right=0
        
        left = right =0
        for i in range(len(s)):
            if s[len(s)-1-i] ==")":
                right+=1
            else:
                left+=1
            
            if left==right:
                ans = max(ans,left*2)

            if right < left:
                left=right=0
                
        return ans
                
                