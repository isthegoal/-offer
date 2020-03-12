# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：   打印一个 二叉树，需要按层次的进行打印        这个没写出来吧

     分析：   这个太明显了，就是层次遍历、或者说是广度优先搜索。

     思路：    还是老知识点，深度优先用栈，广度优先用队列

         我们对一个队列内的元素，首先弹出后进行直接的打印，然后分别把其左子树 和 右子树分别也放到队列中去。 越靠前的层次是越先压到队列的，会越先遍历

'''
def bfs(tree):

    #如果是 空树，直接返回
    if not tree:
        return None

    stack=[tree]#创建 队列来使用，    pop(0)就是 用列表实现的先进先出。

    while stack:
        node=stack.pop(0) #获取队列的首个

        print(node.val)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

