# coding:utf-8
__author__ = 'sin-base'

# 在Python中， 字符串首先是一个序列类型，类似与一个字符数组，字符串是不能改变的，只可以操作为新的字符串
# 也就说，Python在处理字符串的时候，肯定新建立了一个字符串的拷贝，这点在实际性能上，会影响到程序运行

# 常见Python处理字符串的方法
# count         字符串中，子字符串出现的次数
# find          查找字符串 类似的还有 （index、rfind、rindex）
# join          用分隔符合并子串为一个新的字符串
# replace       查找并替换字符串
# split         拆解字符串 类似的还有 splitlines
# startswith    字符串是不是以子串开头 类似的有 endswith
# strip         移除行首行尾的空白符 另请参见 rstrip lstrip
# title         大写每一个单词的第一个字母 另参见 captalize swapcase
# upper         大写整个字符串 类似的有 lower
# isupper       字符串是大写的么 类似的有 islower

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

# 字符串标识符 Python 可以在引号前放置一个标识符 例如 r 代表是一个raw 字符串， 而 u 则代表这是一个Unicode 字符串。
# 这些指示符 (designator) 在编写代码和解释器里显示字符串都非常实用
my_string = u'this is Unicode'
print("designator to String by u", my_string)
# 在打印和转换raw或者 Unicode 字符串的操作是不会打印指示符
# 特别的 raw 告诉解释器不要转换字符串中的任何的特殊字符，例如，特殊字符 \n 通常代表一个新行，但在某些情况下，比如路径不需要这种转换
my_string = r'\w+@\w\.\w+'
print("file path by designator r", my_string)



