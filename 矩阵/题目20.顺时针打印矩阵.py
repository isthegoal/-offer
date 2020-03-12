# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：   面试真题，给你一个矩阵，指定好起始的打印位置，让从一个点开始，顺时针打印出整个矩阵来

     分析：   这题难就难在对邻接点的控制上，分为两大核心：
                【1】每次打圈的邻接的控制，必须让打圈最多到矩阵的中心位置，所以考虑了 打圈的起点的位置来决定次数，这里设定打卷次数的方式，我是万万想不到
                    while start * 2 < rows and start * 2 < cols:
                         print_circle(matrix, start, rows, cols, ret)
                         start += 1
                【2】在限定的圈子和范围内  进行打印，四个for循环就ok了、

     思路：    需要两个函数，一个是打圈函数，   另一个是大的打圈控制函数

'''
def print_matrix(matrix):   #注意如果是 定点开始的，则下面需要多加一次索引位的改变即可
   #分别获取行数row, 列数  col
   rows=len(matrix)
   cols=len(matrix[0] if matrix else 0)

   #打圈起始位置索引
   start=0
   ret=[]   #用于打印的数，其实直接打印即可

   #非常强的  也非常非常重要的打卷次数限制
   while start*2< rows and start*2<cols:
       print_cicle(matrix,start,rows,cols,ret)
       start+=1

   return ret

def print_cicle(matrix,start,rows,cols,ret):
    #现在已经知道 位置点和  临界点， 按照当前的圈位置进行打印即可
    #根据 start索引位置和  行列数结合来 定义 四个锚点位置进行打印

    #首先是定义好终点位置                 起点位置就是start,start
    row=rows-start-1
    col=cols-start-1

    #第一次的从左到右的遍历                   列数变
    for c in range(start,col+1):
        print(matrix[start][c])
        ret.append(matrix[start][c])

    #第二次的  从上往下的遍历，不过多了个if的限制     行数变
    if start<row:
        for r in range(start+1,row+1):
            print(matrix[r][col])
            ret.append(matrix[r][col])

    #第三次，从右往左开始遍历走
    if start<row and start<col:
        for c in range(start,col)[::-1]:  #这个不错，倒着来遍历，很棒的方式，使用[::-1]来实现
            print(matrix[row][c])

    #第四次，  从下往上走进行遍历
    if start<row and start<col:
        for r in range(start+1,row)[::-1]:
            print(matrix[r][start])




