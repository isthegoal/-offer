# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：获取 二叉树的深度

     分析：主要可以使用两种方法吧。
             【1】深度优先遍历。  注意两个点： 遍历时累加，在递归的最后进行还原
             【2】层次遍历。逐层看，并统计层数
'''


#树的深度遍历方式
def get_depth(tree):
    #深度遍历的  空树情况
    if not tree:
        return 0
    #遍历到叶子的情况
    if not tree.left and not tree.right:
        return 1

    #正常的左右比较， 并进行累加的情况。    这样递归的转换子问题思考就行了，  逐步向上。 左右最大加一往上走
    return 1+max(get_depth(tree.left),get_depth(tree.right))

