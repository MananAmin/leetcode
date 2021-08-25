class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mobmap = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        if len(digits)==0:
            return []
        return self.comb(digits,[""],0,mobmap)
    
    def comb(self,digits,prefix,n,mobmap):
        ans = []
        for i in prefix:
            for v in mobmap.get(int(digits[n])):
                ans.append(i+v)
        n+=1
        # print(ans)
        if n > len(digits)-1:
            return ans
        else:
            return self.comb(digits,ans,n,mobmap)