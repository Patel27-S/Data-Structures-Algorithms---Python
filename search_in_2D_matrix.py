# Leetcode 74

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            
            # First find out the right array
            if matrix[i][0] <= target:
                
                # Then perform Binary Search:
                low = 0
                high = len(matrix[i])-1
                mid = (low+high)//2
                
                while high >= low:
                    
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        high = mid-1
                        mid = (low+high)//2
                    else:
                        low = mid+1
                        mid = (low+high)//2
                        
        return False
