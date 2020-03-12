# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格
     ，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
     因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


     分析：直接使用非常简单的回溯法就行了，从（0,0）开始走，分别从上下左右四个方位进行行走。
       如果可以行走，就对 可行走格子总数 +1，同时走过的路，我们设置访问为True,注意这里直接一次统计就行了，相对于66题的判断情况，该题是十分简单的。

      这里的回溯说白了就是深度优先DFS完全遍历，回溯中对满足情况的位置点进行统计。


      就是每走一步时候：   看这个位置点是否以前被行走过，是否是符合要求的机器人可行走的位置。所以需要三个函数就行了。一个是从0,0位置上开始的深度遍历，另一个就是 符合行走要求的判断

'''

class solution:
    #进行  次数统计的总函数。         threshold是限制位数和，rows和cols是行列数
    def movingCount(self,threshold,rows,cols):
        #被不但更新的  已访问visited矩阵
        visited=[False]*(rows*cols)

        #统计开始.      这里设定从0,0开始进行。   得到目标结果
        count=self.movingCountCore(self,threshold,rows,cols,0,0,visited)

        return count


    #进行正式的  从单个点 进行四周扩张形式的统计。    同时对于已经访问过的，当前要避免再访问
    def movingCountCore(self,threshold,rows,cols,row,col,visited):
        #注意这里必须从0开始，因为这是一个回溯的过程，会有非常多无效的尝试，我们只需要统计获取那些有效的统计次数。
        count=0

        #从一个点开始，对附近所有的 四个方位的 未访问点进行查看。
        if self.check(threshold,rows,cols,row,col,visited):
            # 如果当前是可行的且   未被访问时，那就设置现在已经访问过了，统计进行累计到 count中吧
            visited[row*cols+col]=True

            count=1+self.movingCountCore(threshold, rows, cols, row-1, col,visited)+\
                    self.movingCountCore(threshold, rows, cols, row+1, col,visited)+ \
                    self.movingCountCore(threshold, rows, cols, row, col-1,visited) + \
                    self.movingCountCore(threshold, rows, cols, row-1, col+1,visited)
        return count

    # 单独分离出的，验证单个位置点是否合法  且  可行的函数.      三个上面的判断
    def cheack(self,threshold, rows, cols, row, col,visited):
        if row>=0 and row<rows and col>=0 and col<=cols and self.getDigitSum(row)+self.getDigitSum(col)<=threshold and not visited[row*cols+col]:
            return True
        return False


    #最后的用于  辅助的计算 位置点是够是  可运动目标点的函数。
    def getDigitSum(self,number):

        #获取 数字的 位数之和   ,   比如46就是 4+6之和
        sum=0

        while number>0:
            sum+=(number%10)
            number=number//10

        return sum



