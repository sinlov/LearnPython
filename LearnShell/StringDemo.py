# coding:utf-8
__author__ = 'sin-base'

# 在Python中， 字符串首先是一个序列类型，类似与一个字符数组，字符串是不能改变的，只可以操作为新的字符串
# 也就说，Python在处理字符串的时候，肯定新建立了一个字符串的拷贝，这点在实际性能上，会影响到程序运行
s = "this is python learn"
words = s.split()
print("print word by split", words)
print("print word by split", ' '.join(words))
print("print word by split", ' : '.join(words))

# some method by String has, like upper() title() count() find() startswith() replace()
print("print word by split old", s)
print("print word by split upper", s.upper())
print("print word by split title", s.title())
print("print word by split count", s.count('i'))
print("print word by split find lea ", s.find('lea'))
print("print word by split is start with that", s.startswith("that"))
print("print word by split is start with this", s.startswith("this"))
print("print word by split is start with this", s.replace('this', 'that'))

# splintlines() 用于行键切割 rstrip() 用于去掉行末空格
print("print word by split is end with empty", s.splitlines())
print("print word by split is end with empty", s.rstrip())

