# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：   输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径

     分析：这里因为要获取叶子上 累计和，所以最佳好的方法还是  使用深度优先遍历的方法。
             决定主要使用三个信息：
                 [1]树的路径的保存， 用于存储现有的当前走的  路径的 结点访问序列【这里有个trick是每次递归的结束，一定要把push的pop出来，这样其他深度搜才更方便】
                 [2]当前累计综合情况的保存，每次把当前对应搜索序列下 累计总和放到最后一个位置点
     思路：
           不断进行树的深度遍历，可以以脑树的形式理解遍历最形象，  遍历过程中将path和 sums进行保存。
              因此是找到到叶子节点的路径和，所以判断的重要条件就是 到了叶子节点处，判断是够满足总和的条件，满足的话，就打印路径。

            最后要记得 两个列表的pop，因为 要腾位置，你模拟一下就明白了，最后一层左边不行的话，可以弹出来后看看右边。
'''
def find_path(tree,num):
    if not tree:
        return None
    #定义两个  重要的存储路径和  累计和的列表
    path=[tree]
    sums=[tree.val]

    #进行 深度遍历的搜索操作
    def dfs(tree):
        #第一步 针对 非叶子节点，  分别往左和右进行 深的搜素， 同时 保留下累加值以及   路径保存
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1]+tree.left.val)#最新累加值的更新
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1]+tree.right.val)
            dfs(tree.right)

        #第二步 ，较为核心的 针对叶子节点进行判断   累计和是不是需要的
        if not tree.left and not tree.right:
            if sums[-1]==num:
                #满足条件，打印路径即可
                for p in path:
                    print(p)
        #第三步，较为重要的，  递归完之后，一定记得释放位置。    这样下一次递归情况的遍历才正确。  不过N深度下，列表的数量必然是N-1个数量的
        path.pop()
        sums.pop()

    dfs(tree)











