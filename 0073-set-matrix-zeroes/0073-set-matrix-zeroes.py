class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(mat) , len(mat[0])
        row_zero = False
        col_zero = False

        for c in range(n):
            if mat[0][c] == 0:
                row_zero = True
                break

        for r in range(m):
            if mat[r][0] == 0:
                col_zero = True
                break

        for r in range (1,m):
            for c in range (1,n):
                if mat[r][c] == 0:
                    mat[r][0] = 0
                    mat[0][c] = 0
                    
        for r in range(1,m):
            for c in range(1,n):
                if mat[r][0] == 0 or mat[0][c] == 0:
                    mat[r][c] = 0

        if row_zero:
            for c in range(n):
                mat[0][c] = 0

        if col_zero:
            for r in range(m):
                mat[r][0] = 0 