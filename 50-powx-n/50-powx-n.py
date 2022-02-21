class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n<0:
            return 1/self.sol(x,n*-1)
        elif n==0:
            return 1
        else:
            return self.sol(x,n)
        
        
    def sol(self,x,n):
        if n==1:
            return x
        half = self.sol(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x