# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：将二叉搜索树转化成一个排序的双向链表，只调整树中结点的指向【感觉是相当有技巧性的题】


      分析：基本思想 是从形式上做观察，可以发现  二叉搜索树有很多的指向，  而双向链表是每个位置都 有前向 和  后向两个指向。


      思路：可以使用中序遍历的方法，  并令根节点的left指向左子树的  最大值，  right指向 右子树的最小值。【程序也是可以三部分来看待，左遍历，转换指向，右遍历】


      假设二叉搜索树为{10,6,14,4,8,12,16}，按照中序遍历，当我们遍历转换到根节点（值为10的节点）时，它的左子树已经转换成一个排序的链表了，
      并且处在链表的最后一个节点是当前最大的节点。我们把值为8的节点和根节点链接起来，此时链表中的最后一个节点就是10了。接着我们去遍历转换右子树，
      并把根节点和右子树的最小的节点链接起来。转换左子树和右子树，使用递归的方法。
'''
def convert(tree):
    #大的函数
    if not tree:
        return None

    # 核心的 将  二叉树转双向链表的语句
    p_last=convert_node(tree,None)

    #对于 转换后的理解，  利用双向链表的性质，不断左走，走到头结点处
    while p_last and p_last.left:
        p_last=p_last.left

    return p_last

#最为核心的  按照树的性质， 把树不断转成 双向链表的函数。
#   这里  tree含义是当前的树位置，     last可以上一个最后一个最大的
def convert_node(tree,last):
    #根节点 为空时， 返回空
    if not tree:
        return None

    #######转换左子树      这部分用于获取左子树的  最右边的结点，  也就是左子树中最大的结点。
    if tree.left:
        last=convert_node(tree.left,last)


    #######针对  左子树最大的结点实现， 实现两者的互相指向          可以看做中序遍历的转换部分
    if last:
        last.right=tree
    tree.left=last

    #######转换右子树     针对右子树中最小的，让tree的右侧指向它
    last=tree
    if tree.right:
        last=convert_node(tree.right,last)

    return last
