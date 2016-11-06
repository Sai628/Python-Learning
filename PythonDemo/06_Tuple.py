# coding=utf-8

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup3 = "a", "b", "c", "d"
tup4 = ()
tup5 = (50,)

print "tup1[0]:", tup1[0]  # tup1[0]: physics
print "tup2[1:5]:", tup2[1:5]  # tup2[1:5]: (2, 3, 4, 5)


tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# the following operation of update tuple element is illegal
# tup1[0] = 100

tup3 = tup1 + tup2
print tup3  # (12, 34.56, 'abc', 'xyz')


tup = ('physics', 'chemistry', 1997, 2000)
print tup  # ('physics', 'chemistry', 1997, 2000)
del tup

try:
    print "After deleting tup:"  # After deleting tup:
    print tup
except Exception, e:
    print Exception, e  # <type 'exceptions.Exception'> name 'tup' is not defined


# Tuple Operator
print len((1, 2, 3))  # 3
print (1, 2, 3) + (4, 5, 6)  # (1, 2, 3, 4, 5, 6)
print ('Hi!',) * 4  # ('Hi!', 'Hi!', 'Hi!', 'Hi!')
print 3 in (1, 2, 3)  # True

for x in (1, 2, 3):
    print x
# 1
# 2
# 3


L = ('spam', 'Spam', 'SPAM!')
print L[2]  # SPAM!
print L[-2]  # Spam
print L[1:]  # ('Spam', 'SPAM!')


print 'abc', -4.24e93, 18+6.6j, 'xyz'  # abc -4.24e+93 (18+6.6j) xyz
x, y = 1, 2
print "Value of x, y:", x, y  # Value of x, y: 1 2


# Tuple Build-in Functions
tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
print cmp(tuple1, tuple2)  # -1
print cmp(tuple2, tuple1)  # 1
tuple3 = tuple2 + (786,)
print cmp(tuple2, tuple3)  # 1


tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print "First tuple lenght:", len(tuple1)  # First tuple lenght: 3
print "Second tuple lenght:", len(tuple2)  # Second tuple lenght: 2


tuple1, tuple2 = (123, 'xyz', 'zara', 'abc'), (456, 700, 200)
print "Max value element of tuple1:", max(tuple1)  # Max value element of tuple1: zara
print "Max value element of tuple2:", max(tuple2)  # Max value element of tuple2: 700
print "Min value element of tuple1:", min(tuple1)  # Min value element of tuple1: 123
print "Min value element of tuple2:", min(tuple2)  # Min value element of tuple2: 200


aList = [123, 'xyz', 'zara', 'abc']
aTuple1 = tuple(aList)
print "Tuple1 elements:", aTuple1  # Tuple1 elements: (123, 'xyz', 'zara', 'abc')

aDict = {1: 2, 3: 4}
aTuple2 = tuple(aDict)  # for a dict, the "tuple" function will return a tuple consists of the keys of the dict
print "Tuple2 elements:", aTuple2  # Tuple2 elements: (1, 3)



