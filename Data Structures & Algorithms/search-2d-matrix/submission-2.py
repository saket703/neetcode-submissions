class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined=[]
        for i in matrix:
            combined+=i
        if target in combined:
            return True
        else:
            return False