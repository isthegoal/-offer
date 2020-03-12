# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：  判断一棵二叉树是不是另一个的子结构

     分析：  这种树的问题，很明显是使用递归的方法，这里对 大树要做完全的遍历，同时考虑大树的左和右，完全的遍历下就能克服只包含  部分结点的情况。
             我们的目标是找到使得Tree2子树为空的情况。
                    同时如果遇到Tree1为空，而Tree2不为空的情况说明查找失败。

     思路还是比较很有技巧的

     思路：  这里有几个控制，话不多说，看代码吧，主要就三个控制需要注意.     这里  使用tree2的不同部分参与比较，整体递归的时间复杂度还是挺高的，但是也没办法。
     时间复杂度是 o(N)吧，所有节点都比较

'''

def sub_tree(tree1,tree2):
    #在 两个  树都不为空的情况下
    if tree1 and tree2:
        #在  不为空时，还包括两种情况，一种是   当前节点  值相同
        if tree1.val==tree2.val:
            #考虑的可能是子树的情况      此时是强要求， 必须要求新子问题下，两个树都得是完全满足左右都相同的情况
            return sub_tree(tree1.left,tree2.left) and sub_tree(tree1.right and tree2.right)

        #另一种是  当前不相等，那么 可以    继续的探索， 这里的探索使用or方式，较为松散方式的要求即可
        else:
            return sub_tree(tree1.left,tree2) or sub_tree(tree1.right,tree2)

    #有 一个树 为空时，有两种情况，1树空，2树不空是 查找失败的情况
    if not  tree1 and tree2:
        return False
    #第二种是其他的都看作查找  成功的情况
    return True