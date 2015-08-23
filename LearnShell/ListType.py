# coding:utf-8
__author__ = 'sinlov'

# python 中含有一个类型是列表类型，列表是可变的序列，可以保存任何类型
book = ['python', 'Development', 8, 2008]
book.insert(1, 'web')
print("print book list", book)
print("print book list slicing ", book[:2])

# check object is in list
print("is python in book?", 'python' in book)

# remove object
my_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
print("from my_list full", my_list)
my_list.remove('w')
print("from my_list remove item 'w'", my_list)
my_list.pop(2)
print("from my_list remove item by index", my_list)

# copy list by '*'
copy_list = ['a', 's', 'd']
print("this is one list to copy begin", copy_list)
print("this is one list to copy after", copy_list * 2)
# extend this list
copy_list.extend(['f', 'g'])
print("list copy list can extend", copy_list)

# can sort this list
for_sort = ['python', 'Development', 8, 2008, 'web']
print("list for sort before", for_sort)
for_sort.sort()
print("list for sort before", for_sort)
# python 对于未指定的混合序列，排序是不定的，默认顺序是，先对所有数字进行排序，然后对于字符串按照字典排序，
# 如果是对象类型，则非常混乱
# 列表中，内置函数， sort() append() insert 都是直接对对象进行修改，没有返回值。所以，直接打印 list.soft() 会返回none。
# 而字符串的操作函数，如 upper() 是返回一个字符串（其实是包含一个全部是大写的字符串拷贝，所以未对原有字符串对象进行修改，
# 新增了一个字符串）如果是希望得到一个排好序的拷贝，
# 使用 sorted() 或者 reversed
# 分别意思为接受一个列表作为参数并返回一个排好序的或者倒序的拷贝
# list comprehension 是一个由逻辑代码组成的结构， 包含一段逻辑代码生成的值或者对象

# list comperhension 列推导
data = [x + 1 for x in range(10)]
print("list comperhension", data)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("list comperhenison by double", even_numbers)
# 这种写法常用于过滤表达式 其中 x 本身就是一个表达式值

# generator expression
generator_number = (x for x in range(10000) if x % 2 == 0)
print("generator numbers print", generator_number)

