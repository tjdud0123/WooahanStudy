## ## 10-9) Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

def findTarget2(matrix, target):
    ROW, COL = len(matrix), len(matrix[0])
    i, j = 0, COL-1
    while i < ROW and j >= 0:
        cur_num = matrix[i][j]
        # 탐색 성공
        if cur_num == target:
            return (i, j)
        # next 
        if cur_num > target:
            j -= 1
        else:
            i += 1
    # 탐색 실패
    return None