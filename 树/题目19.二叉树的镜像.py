# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

#    deque双向队列模块：   python标准库collections中的一项，它提供了两端都可以操作的序列，这意味着，在序列的前后你都可以执行添加或删除操作。
'''
     题目：   输入二叉树，输出它的镜像

     分析：   感觉这种镜像打印是 十分简单的，基本思路就是 遍历 +  先右后做，最为直观的思路是使用层次遍历[使用队列实现即可]，   对于每一层从右往左进行打印

     思路：   两种思路吧， 分别是   从右到左的层次遍历
                                  递归的方式
                                  
              可以实现本身上转成 镜像树，或者按照镜像后的结果进行层次的遍历打印

'''
from collections import deque
#第一种  从右到左的层次遍历  方式
def mirrot_bfs(root):
    #首先 设定是 使用一个 双向队列。      可以双端打印的，使用不同的pop
    queue=deque(root)

    #预存  镜像打印的序列
    ret=[]

    #开始不断的进行  弹出  并打印
    while queue:
        node=queue.popleft() #按队列形式   每次打印最先放到队列中的一个


        if node:
            #类似于print放前面，把每一层的先放前面， 每一层的所有先放到队列，才能保证层次遍历
            ret.append(node)

            #层次的核心实现，
            queue.append(node.right)
            queue.append(node.left)

    return ret



#第二种方法    递归的方式        但是这种可以实现镜像的打印吗，感觉有些奇怪。   还是非递归的方式实现的  层次遍历感觉有意思。这个 好像有点问题
ret=[]
#递归方式，  生成新的镜像树     这里就是不断的实现交换即可    这样就可以得到镜像的结果了
def travel(root):
    #递归的方式
    if root == None:
        root.left,root.right=root.right,root.left

        if root.left:
            travel(root.left)
        if root.right:
            travel(root.right)

