# coding=utf-8

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter  #100
print miles  #1000.0
print name  # John

a = b = c = 1
a, b, c = 1, 2, "John"


# Number
var1 = 1
var2 = 10
del var1
del var2

# String
str = 'Hello World!'

print str  #Hello World!
print str[0]  #H
print str[2:5]  #llo
print str[2:]  #llo World!
print str * 2  #Hello World!Hello World!
print str + "TEST"  #Hello World!TEST

# List
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  #['abcd', 786, 2.23, 'john', 70.2]
print list[0]  #abcd
print list[1:3]  #[786, 2.23]
print list[2:]  #[2.23, 'john', 70.2]
print tinylist * 2  #[123, 'john', 123, 'john']
print list + tinylist  #['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

# Tuple
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple  #('abcd', 786, 2.23, 'john', 70.2)
print tuple[0]  #abcd
print tuple[1:3]  #(786, 2.23)
print tuple[2:]  #(2.23, 'john', 70.2)
print tinytuple * 2  #(123, 'john', 123, 'john')
print tuple + tinytuple  #('abcd', 786, 2.23, 'john', 70.2, 123, 'john')

# Dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  #This is one
print dict[2]  #This is two
print tinydict  #{'dept': 'sales', 'code': 6734, 'name': 'john'}
print tinydict.keys()  #['dept', 'code', 'name']
print tinydict.values()  #['sales', 6734, 'john']


