# coding=utf-8

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print "list1[0]:", list1[0]  # list1[0]: physics
print "list2[1:5]:", list2[1:5]  # list2[1:5]: [2, 3, 4, 5]

list1[2] = 2001
print list1[2]  # 2001

print list1  # ['physics', 'chemistry', 2001, 2000]
del list1[2]
print "After deleting value at index 2:", list1  # After deleting value at index 2: ['physics', 'chemistry', 2000]


print len([1, 2, 3])  # 3
print [1, 2, 3] + [4, 5, 6]  # [1, 2, 3, 4, 5, 6]
print ['Hi!'] * 4  # ['Hi!', 'Hi!', 'Hi!', 'Hi!']
print 3 in [1, 2, 3]  # True

for x in [1, 2, 3]:
    print x
# 1
# 2
# 3


L = ['one', 'two', 'three']
print L[2]  # three
print L[-2]  # two
print L[1:]  # ['two', 'three']


# List Function & Method
list1, list2 = [123, 'xyz'], [456, 'abc']
print cmp(list1, list2)  # -1
print cmp(list2, list1)  # 1
list3 = list2 + [789]
print cmp(list2, list3)  # -1

list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print len(list1)  # 3
print len(list2)  # 2

list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
print max(list1)  # zara
print max(list2)  # 700
print min(list1)  # 123
print min(list2)  # 200

aTuple = (123, 'xyz', 'zara', 'abc')
print list(aTuple)  # [123, 'xyz', 'zara', 'abc']

aList = [123, 'xyz', 'zara', 'abc']
aList.append(2009)
print aList  # [123, 'xyz', 'zara', 'abc', 2009]

aList = [123, 'xyz', 'zara', 'abc', 123]
print aList.count(123)  # 2
print aList.count('zara')  # 1

bList = [2009, 'manni']
aList.extend(bList)
print aList  # [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']

aList = [123, 'xyz', 'zara', 'abc']
print aList.index('xyz')  # 1
print aList.index('zara')  # 2
try:
    print aList.index('test')
except Exception, e:
    print Exception, e  # <type 'exceptions.Exception'> 'test' is not in list

aList.insert(3, 2009)
print aList  # [123, 'xyz', 'zara', 2009, 'abc']

aList = [123, 'xyz', 'zara', 'abc']
print aList.pop()  # abc
print aList.pop(1)  # xyz
print aList  # [123, 'zara']

aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print aList  # [123, 'zara', 'abc', 'xyz']
aList.remove('abc')
print aList  # [123, 'zara', 'xyz']

aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print aList  # ['xyz', 'abc', 'zara', 'xyz', 123]

aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.sort()
print aList  # [123, 'abc', 'xyz', 'xyz', 'zara']
