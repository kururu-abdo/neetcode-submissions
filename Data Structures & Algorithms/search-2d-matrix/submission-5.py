class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for matr in range(len(matrix)):
            left =0
            right = len(matrix[matr]) -1
            arr = matrix[matr]
            if not arr:
                continue
            
            if len(arr) <=1 and arr[0] != target:
                continue

            while(left<=right):
                middle = left + (right - left) // 2
                if target == arr[middle]:
                    return True
                elif arr[middle]<target:
                    left = middle+1
                else:
                    right = middle - 1






        return False