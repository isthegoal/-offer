# coding: utf-8

'''

         题目：  二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中

         思路：  从左下角或者右上角开始比较
'''

def find_max(matrix,num):
    #使用左下角  进行查找。   如果小于就往上走，如果大于就右走  即可。  这样很简单就能得到结果[特别简单的遍历即可]
    if not matrix:
        return False

    rows,cols= len(matrix),len(matrix[0])

    row,col=rows-1,0

    while row>=0 and col<=cols-1:
        if matrix[row][col]==num:
            return True
        elif matrix[row][col]>num:
            row-=1
        else:
            col-=1
    return False
