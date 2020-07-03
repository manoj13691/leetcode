# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_ans = -1
        
        if not matrix:
            return 0
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        dp = [[0]*col_len for i in range(row_len)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = self.helper2(matrix, i, j, row_len, col_len, dp)
                if ans > max_ans:
                    max_ans = ans
        return (max_ans)
    
    
    def helper2(self, matrix, row, col, row_len, col_len, dp):
        if row >= row_len or row <0 or col >=col_len or col <0:
            return 0
        
        if dp[row][col]!=0:
            return dp[row][col]
        
        cur_val = matrix[row][col]

        right = self.helper2(matrix, row, col+1, row_len, col_len, dp) if col+1 < col_len and matrix[row][col+1] > cur_val else 0
        left = self.helper2(matrix, row, col-1, row_len, col_len, dp) if col-1 >=0 and matrix[row][col-1] > cur_val else  0
        up = self.helper2(matrix, row-1, col, row_len, col_len, dp) if row-1 >=0 and matrix[row-1][col] > cur_val  else  0
        down = self.helper2(matrix, row+1, col, row_len, col_len, dp) if row+1 < row_len and matrix[row+1][col] > cur_val else  0

        dp[row][col] = 1 + max(left, right, up, down)
        return dp[row][col]
    
    
    
    def helper(self, matrix, row, col, row_len, col_len):
        if row >= row_len or row <0 or col >=col_len or col <0:
            return 0
        
        cur_val = matrix[row][col]
        
        right = self.helper(matrix, row, col+1, row_len, col_len) if col+1 < col_len and matrix[row][col+1] > cur_val else 0
        left = self.helper(matrix, row, col-1, row_len, col_len) if col-1 >=0 and matrix[row][col-1] > cur_val else  0
        up = self.helper(matrix, row-1, col, row_len, col_len) if row-1 >=0 and matrix[row-1][col] > cur_val  else  0
        down = self.helper(matrix, row+1, col, row_len, col_len) if row+1 < row_len and matrix[row+1][col] > cur_val else  0
        
        return 1 + max(left, right, up, down)
        
        
        
