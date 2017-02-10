# coding=utf-8


counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter  # 100
print miles  # 1000.0
print name  # John

a = b = c = 1
a, b, c = 1, 2, "John"


# Python 有5种标准的数据类型: 数字, 字符串, 列表, 元组, 字典
# Number
var1 = 1
var2 = 10
del var1
del var2


# String
mystr = 'Hello World!'

print mystr  # Hello World!
print mystr[0]  # H
print mystr[2:5]  # llo
print mystr[2:]  # llo World!
print mystr * 2  # Hello World!Hello World!
print mystr + "TEST"  # Hello World!TEST
print mystr[-3:]  # ld!


# List
mylist = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print mylist  # ['abcd', 786, 2.23, 'john', 70.2]
print mylist[0]  # abcd
print mylist[1:3]  # [786, 2.23]
print mylist[2:]  # [2.23, 'john', 70.2]
print tinylist * 2  # [123, 'john', 123, 'john']
print mylist + tinylist  # ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
print tinylist + mylist  # [123, 'john', 'abcd', 786, 2.23, 'john', 70.2]


# Tuple
mytuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print mytuple  # ('abcd', 786, 2.23, 'john', 70.2)
print mytuple[0]  # abcd
print mytuple[1:3]  # (786, 2.23)
print mytuple[2:]  # (2.23, 'john', 70.2)
print tinytuple * 2  # (123, 'john', 123, 'john')
print mytuple + tinytuple  # ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
print tinytuple + mytuple  # (123, 'john', 'abcd', 786, 2.23, 'john', 70.2)


# Dictionary
mydict = {}
mydict['one'] = "This is one"
mydict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print mydict['one']  # This is one
print mydict[2]  # This is two
print tinydict  # {'dept': 'sales', 'code': 6734, 'name': 'john'}
print tinydict.keys()  # ['dept', 'code', 'name']
print tinydict.values()  # ['sales', 6734, 'john']
