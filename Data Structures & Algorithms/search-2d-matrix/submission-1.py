class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = -1

        for i in range(len(matrix)):
            big = matrix[i][-1] # last element per row
            if target <= big: # i is the row we want
                j = i
                break
        
        k = 0
        
        while k <= len(matrix[j]) - 1:
            curr = matrix[j][k]
            if curr == target:
                return True
            k += 1

        return False
        
        