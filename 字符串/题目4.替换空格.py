# coding: utf-8

'''
     把字符串'a b  b'中的空格替换成'20%'
'''

#方法一.使用python内置的replace函数即可
print('a b  b'.replace(' ','20%'))

#方法二.使用正则表达式进行替换         这里注意好re进行compile后的用法即可
import re
ret=re.compile(' ')
ret.sub('20%','a b  b')