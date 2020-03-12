'''
     题目：  把字符串转化成整数,如果是合法的数值表达则返回该数字，否则返回0

     字符串可以包含： 正负数、0、空字符、  其他字符。
       输入   比如   +2147483647    对应输出为  2147483647
       输入   比如   1a33    对应输出为  0

     分析： 现在逐个的，按照遇到的字符，将字符转成数字。
           针对遇到的字符，我们主要从以下五个问题进行考虑。
           （1）指针是否为空指针以及字符串是否为空字符串；
           （2）字符串对于正负号的处理；
           （3）输入值是否为合法值，即小于等于'9'，大于等于'0'；
           （4）int为32位，需要判断是否溢出；
           （5）使用错误标志，区分合法值0和非法值0。
'''


def str_to_int(string):
    #首先思考边缘条件
    length=len(string)
    if length==0:
        return

    #正常情况下的逐个判断
    else:
        minus=False
        flag=False

        #首先是考虑正负号的情况
        if string[0]=='+':
            flag=True
        if string[0]=='-':
            flag=True
            minus=True

        #初始索引位置，  如果有符号为，那就从1索引开始
        begin = 0
        if flag:
            begin=1

        #最后的按 位 累加数
        num=0

        # 对正负号情况的判别
        minus = -1 if minus else 1

        for each in string[begin:]:
            #直接拼接得到数字吧
            if each>='0' and each<='9':
                #这里  minus 是累加时考虑的对应位，这里的ord表示返回字符的ASCII码
                num=num*10+ minus*(ord(each)-ord('0'))
            else:
                #遇到违法字符时，那就说明整个有问题，直接退出吧
                num=0
                break
        return num





