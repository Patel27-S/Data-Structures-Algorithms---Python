# Leetcode 48

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix[0])
        
        for i in range(n):
            for j in range(i,len(matrix)-1):
                matrix[i][j+1], matrix[j+1][i] = \
                matrix[j+1][i], matrix[i][j+1]   
                
        # Mirroring of all the array elements of each of the 
        # arrays in the matrix
        for array in matrix:
            i = 0
            j = len(array)-1
            
            while j >= i:
                array[i], array[j] = \
                array[j], array[i]
                j -= 1
                i += 1
                
