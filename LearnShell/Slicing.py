# coding:utf-8
__author__ = 'sinlov'
s = 'python'

# 此种切片方式适用于一切序列类型
print("slicing string by 1 to 4", s[1:4])
print("slicing string by 0 to 4  hide front", s[:4])
print("slicing string by 3 to null hide back", s[3:])
print("slicing string by 3 to -1 roll back", s[3:-1])
print("slicing string by null to null full like copy", s[:])
print("slicing string by str() copy", str(s))

# 作用于序列之上的操作还可以是 连接 (+) 复制 (*) 以及检查成员的 (in 和 not in) 例如如下的写法
print("slicing by operation + ", 'python and ' + 'Django are fast')
print("slicing by operation + more ", 'python and ' + '   ' + 'Django are fast!')
print("slicing by operation *", '-' * 20)
print("slicing by operation in", 'an' in 'Django')
print("slicing by operation not in", 'an' not in 'Django')

# 注意 建议避免在使用序列时使用(+) 操作符，因为效率不高（原因是Python在C下的实现）如果要使用字符串拼接的话，使用 '%'来取代，另一种方法是
# join() 来操作，如果是一个列表 extend() 方法也很好用