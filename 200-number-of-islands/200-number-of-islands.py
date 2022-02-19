class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        return self.sol(grid)
    
    
    def dfs(self,i,j,grid):
        
        if i<0 or i>len(grid)-1 or j<0 or j >len(grid[0])-1 or grid[i][j] !="1":
            return
        grid[i][j] = -1
        
        self.dfs(i+1,j,grid)
        self.dfs(i,j+1,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i,j-1,grid)
        
        
    def sol(self,grid):
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]=="1":
                    count+=1
                    self.dfs(i,j,grid)
        return count