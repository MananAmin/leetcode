# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n==0:
            return [[]]
        
        return self.dfs_sol(1,n+1)
    
    def dfs_sol(self,start,end):
        
        if start ==end:
            return None
        
        result = []
        for i in range(start,end):
            for l in self.dfs_sol(start,i) or [None]:
                for r in self.dfs_sol(i+1,end) or [None]:
                    node  = TreeNode(i)
                    node.left = l
                    node.right = r
                    result.append(node)
        return result