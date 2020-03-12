# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径

      路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，
      则该路径不能再进入该格子。 例如在下面的3x4的矩阵中包含一条字符串"bcced"的路径（路径中的字母用斜体表示）。但是矩阵中不包含"abcb"路径，
      因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

                               a   b   c   e
                               s   f   c   s
                               a   d   e   e


     分析： 任选一个格子作为路径的起点。

     [1]回溯法。任选一个格子作为路径的起点。假设矩阵中某个格子的字符为ch并且这个格子将对应于路径上的
     第i个字符。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。如果路径上的第i个字符
     正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子外，其他各自都有4个相邻的格子。
     重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。


         这里主要是两个函数：
           【1】haspath函数用于遍历   以这个矩阵中所有的位置点开始行走，能够走到位置点的情况。这里注意是从位置点开始
           【2】haspathCore函数用于针对 haspath所提供的起点位置，进行从起点位置开始的四个方向的探索，探索中标记已探索。
           通过不断的回溯，进行深度优先遍历DFS过程，不断探索四个方位行走的效果，并不断进行回溯的还原，就可以得到通过在一个位置作为起点的
           深度优先扩展下，是否可以延伸出目标path路径。

           思想非常非常的简单，就是尝试以每个位置点作为起点， 用回溯的方法尝试以点作为起点是够可以走出目标的path路径。
'''
class solution:

    # 核心的判断是否 有 路径的主函数。  对所有矩阵位置的逐个遍历。
    def haspath(self,matrix,rows,cols,path):
        #边缘条件
        if matrix==None or rows<1 or cols<1 or path == None:
            return False

        #定义  访问记录矩阵     注意这里的visited会在后面的函数调用中 不断进行更新，这个是性质吧，python不需要明显指明传递实参
        visited=[0]*(rows*cols)

        #这里是对 所有的起点情况 进行考虑，  考虑从该起点行走是否能够走出需求的路径。
        pathlength=0
        for row in range(rows):
            for col in range(cols):
                print('每次：',visited)
                print('每：', pathlength)
                #如果能找到一个是存在的， 成功的，就ok
                if self.haspathCore(matrix,rows,cols,row,col,path,pathlength,visited):
                    return True
        return False

    #额外的主要的进行判别的函数，  对于第一个函数haspath的每个起点开始进行遍历查找。
    def haspathCore(self,matrix,rows,cols,row,col,path,pathlength,visited):
        #这里pathlength是已经行走的长度，  len(path)是目标路径长度，当两者相同则说明自己成功走的长度够了，结束即可。
        if len(path)==pathlength:
            return True

        hasPath=False

        #我们对于不同的起点 位置，开始进行判断从这个点开始的行走寻找，是否可以逐步到达目标探索结果。
        #当前判别条件就是，必须位置在矩阵内，同时没有被探索过，而且所在的点是path目标内的对应点，是正确的路径
        if row>=0 and row<rows and col>=0 and col<cols and matrix[row*cols+col]==path[pathlength] and not visited[row*cols+col]:
            #当初步满足时，我们继续往后走
            pathlength+=1
            visited[row*cols+col]=True

            #在当前尝试对  上下左右四个方位进行探索。四个方位上，只要有一个可以进行行走能走到目的地的都行，会不断回溯，如果在单个方位怎么走都走不出剩余路径，那就False了。
            hasPath=self.haspathCore(matrix,rows,cols,row,col-1,path,pathlength,visited) or self.haspathCore(matrix,rows,cols,row-1,col,path,pathlength,visited) or self.haspathCore(matrix,rows,cols,row,col+1,path,pathlength,visited) or self.haspathCore(matrix,rows,cols,row+1,col,path,pathlength,visited)

            #当不存在路径时， 进行回归，回溯，同时设置当前位置是被探索过的，不能被走出path的。
            #这里的回溯非常重要，对于每次深入的探索，如果无效时，我们需要对自己行走过得路进行visit还原，对path行走积攒还原。
            if not hasPath:
                pathlength-=1
                visited[row*cols+col]=False

        return hasPath

s = solution()
ifTrue = s.haspath("ABCESFCSADEE", 3, 4, "ABCCED")
print('咕噜咕噜')
ifTrue2 = s.haspath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
