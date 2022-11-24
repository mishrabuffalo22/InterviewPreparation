class Solution:
    def recur(self, board,i,j,l,word):
        if i>len(board)-1 or j>len(board[0])-1 or i<0 or j<0 or board[i][j]==-1 or l>len(word)-1:
            return 0
        if board[i][j]!=word[l]:
            return 0
        if l==len(word)-1:
            return 1
        d = board[i][j]
        board[i][j] = -1
        
        up = self.recur(board,i,j-1,l+1,word)
        if up:
            board[i][j] = d
            return 1
        down = self.recur(board,i,j+1,l+1,word)
        if down:
            board[i][j] = d
            return 1
        left = self.recur(board,i-1,j,l+1,word)
        if left:
            board[i][j] = d
            return 1
        right = self.recur(board,i+1,j,l+1,word)
        if right:
            board[i][j] = d
            return 1
        board[i][j] = d
        return 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.recur(board,i,j,0,word):
                        return 1
        return 0
        