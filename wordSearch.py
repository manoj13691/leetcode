# https://leetcode.com/problems/word-search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = self.dfs(board, word, i, j, 0)
                if res:
                    return True
        return False
       
    
    def dfs(self, board, word, i, j, index):
        
        if index>=len(word):
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return False

        
        if board[i][j]!=word[index]:
            return False
        
        # now character at (i,j) in board is equal to word[index].
        # so we need check for next characters from here.
        # during dfs call we might want to use visited to not visit cell again
        # or we can change the value to # so that it wont match the character.
        # but after the calls, we need to change it back to original value
        # for further dfs calls
        
        cur_val = board[i][j]
        
        board[i][j] = '#'
        
        res = self.dfs(board, word, i+1, j, index+1) or self.dfs(board, word, i-1,j, index+1) or self.dfs(board, word, i, j+1, index+1) or self.dfs(board, word, i, j-1, index+1)
        board[i][j] = cur_val
        return res
    
