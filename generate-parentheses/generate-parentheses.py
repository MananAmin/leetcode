class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n==1:
            return ["()"]
        res = []
        self.paren(n,0,0,"",res)
        return res
    
    def paren(self,n,op,cl,cur,res):
        
        if len(cur) == n*2:
            res.append(cur)
            return
        
        if op<n:
            self.paren(n,op+1,cl,cur+"(",res)
        if cl<op:
            self.paren(n,op,cl+1,cur+")",res)
        return