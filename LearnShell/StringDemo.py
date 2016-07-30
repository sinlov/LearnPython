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

# 去空格及特殊符号
s.strip().lstrip().rstrip(',')

# 复制字符串
# strcpy(sStr1,sStr2)
sStr1 = 'strcpy'
sStr2 = sStr1
sStr1 = 'strcpy2'
print sStr2

# 连接字符串
# strcat(sStr1,sStr2)
sStr1 = 'strcat'
sStr2 = 'append'
sStr1 += sStr2
print sStr1

# 查找字符
# strchr(sStr1,sStr2)
# < 0 为未找到
sStr1 = 'strchr'
sStr2 = 's'
nPos = sStr1.index(sStr2)
print nPos

# 比较字符串
# strcmp(sStr1,sStr2)
sStr1 = 'strchr'
sStr2 = 'strch'
print cmp(sStr1, sStr2)

# 扫描字符串是否包含指定的字符
# strspn(sStr1,sStr2)
sStr1 = '12345678'
sStr2 = '456'
# sStr1 and chars both in sStr1 and sStr2
print len(sStr1 and sStr2)

# 字符串长度
# strlen(sStr1)
sStr1 = 'strlen'
print len(sStr1)

# 将字符串中的大小写转换
# strlwr(sStr1)
sStr1 = 'JCstrlwr'
sStr1 = sStr1.upper()
# sStr1 = sStr1.lower()
print sStr1

# 追加指定长度的字符串
# strncat(sStr1,sStr2,n)
sStr1 = '12345'
sStr2 = 'abcdef'
n = 3
sStr1 += sStr2[0:n]
print sStr1

# 字符串指定长度比较
# strncmp(sStr1,sStr2,n)
sStr1 = '12345'
sStr2 = '123bc'
n = 3
print cmp(sStr1[0:n], sStr2[0:n])

# 复制指定长度的字符
# strncpy(sStr1,sStr2,n)
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print sStr1

# 将字符串前n个字符替换为指定的字符
# strnset(sStr1,ch,n)
sStr1 = '12345'
ch = 'r'
n = 3
sStr1 = n * ch + sStr1[3:]
print sStr1

# 扫描字符串
# strpbrk(sStr1,sStr2)
sStr1 = 'cekjgdklab'
sStr2 = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr2:
        nPos = sStr1.index(c)
        break
print nPos

# 翻转字符串
# strrev(sStr1)
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print sStr1
# 查找字符串
# strstr(sStr1,sStr2)
sStr1 = 'abcdefg'
sStr2 = 'cde'
print sStr1.find(sStr2)

# 分割字符串
# strtok(sStr1,sStr2)
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2) + 1:]
print sStr1
# 或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))

# 连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
# PHP 中 addslashes 的实现
def addslashes(s):
    d = {'"': '\\"', "'": "\\'", "\0": "\\\0", "\\": "\\\\"}
    return ''.join(d.get(c, c) for c in s)


s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s
print addslashes(s)

# 只显示字母与数字
def OnlyCharNum(s, oth=''):
    s2 = s.lower()
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c, '')
    return s


print(OnlyCharNum("a000 aa-b"))


# 截取字符串
str = '0123456789'
print str[0:3]  # 截取第一位到第三位的字符
print str[:]  # 截取字符串的全部字符
print str[6:]  # 截取第七个字符到结尾
print str[:-3]  # 截取从头开始到倒数第三个字符之前
print str[2]  # 截取第三个字符
print str[-1]  # 截取倒数第一个字符
print str[::-1]  # 创造一个与原字符串顺序相反的字符串
print str[-3:-1]  # 截取倒数第三位与倒数第一位之前的字符
print str[-3:]  # 截取倒数第三位到结尾
print str[:-5:-3]  # 逆序截取，具体啥意思没搞明白？

# 打印boolean 类型会提示错误,无法拼接
res = ['change Log print success at => ', 'False']
print "".join(res)
