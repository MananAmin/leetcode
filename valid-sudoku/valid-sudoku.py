class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.first_sol(board)
        
        
    def first_sol(self,board):
        
#         check for vertical and horizontal
        for i in range(9):
            checkv = [False]*10
            checkh = [False]*10
            for j in range(9):
                if board[i][j] !="." and not checkh[int(board[i][j])]:
                    checkh[int(board[i][j])] = True
                elif board[i][j] !=".":
                    return False
                
                if board[j][i] !="." and not checkv[int(board[j][i])]:
                    checkv[int(board[j][i])] = True
                elif board[j][i] !=".":
                    return False
        print("here")
        
        for h in range(3):
            for v in range(3):
                starth = 3*h
                startv = 3*v
                print("start ",starth, " ",startv)
                check = set()
                for i in range(3):
                    for j in range(3):
                        if board[starth+i][startv+j] !="." and not board[starth+i][startv+j] in check:
                            check.add(board[starth+i][startv+j])
                        elif board[starth+i][startv+j] !=".":
                            # print("herrrre" ,i," ",j)
                            return False
        return True
                            