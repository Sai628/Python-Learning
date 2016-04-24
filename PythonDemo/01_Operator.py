# coding=utf-8

# Arithmetic operator
a = 21
b = 10
c = 0

c = a + b
print c  # 31

c = a - b
print c  # 11

c = a * b
print c  # 210

c = a / b
print c  # 2

c = a % b
print c  # 1

a = 2
b = 3
c = a ** b
print c  # 8

a = 10
b = 5
c = a // b
print c  # 2


# Relational operator
a = 21
b = 10
c = 0

if a == b:
    print "a==b"
else:
    print "a!=b"  # a!=b

if a != b:
    print "a!=b"  # a!=b
else:
    print "a==b"

if a < b:
    print "a<b"
else:
    print "a>=b"  # a>=b

if a > b:
    print "a>b"  # a>b
else:
    print "a<=b"


a = 5
b = 20
if a <= b:
    print "a<=b"  # a<=b
else:
    print "a>b"

if b >= a:
    print "b>=a"  # b>=a
else:
    print "b<a"


# Assign operator
a = 21
b = 10
c = 0

c = a + b
print c  # 31

c += a
print c  # 52

c *= a
print c  # 1092

c /= a
print c  # 52

c = 2
c %= a
print c  # 2

c **= a
print c  # 2097152

c //= a
print c  # 99864


# Bitwise operator
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b
print c  # 12 = 0000 1100

c = a | b
print c  # 61 = 0011 1101

c = a ^ b
print c  # 49 = 0011 0001

c = ~a
print c  # -61 = 1100 0011

c = a << 2
print c  # 240 = 1111 0000

c = a >> 2
print c  # # 15 = 0000 1111


# Logical operator
a = 10
b = 20

if a and b:
    print "'a and b' is true"  # 'a and b' is true
else:
    print "'a and b' is false"

if a or b:
    print "'a or b' is true"  # 'a or b' is true
else:
    print "'a or b' is false"

a = 0
if a and b:
    print "'a and b' is true"
else:
    print "'a and b' is false"  # 'a and b' is false

if a or b:
    print "'a or b' is true"  # 'a or b' is true
else:
    print "'a or b' is false"

if not(a and b):
    print "'not(a and b)' is true"  # 'not(a and b)' is true
else:
    print "'not(a and b)' is false"


# Member operator
a = 10
b = 20
mylist = [1, 2, 3, 4, 5]

if a in mylist:
    print "a in mylist"
else:
    print "a not in mylist"  # a not in mylist

if b not in mylist:
    print "b not in mylist"  # b not in mylist
else:
    print "b in mylist"

a = 2
if a in mylist:
    print "a in mylist"  # a in mylist
else:
    print "a not in mylist"


# Identity operator
a = 20
b = 20

if a is b:
    print "a and b has the same identity"  # a and b has the same identity
else:
    print "a and b has different identity"

if id(a) == id(b):
    print "a and b has the same identity"  # a and b has the same identity
else:
    print "a and b has different identity"

b = 30
if a is b:
    print "a and b has the same identity"
else:
    print "a and b has different identity"  # a and b has different identity

if a is not b:
    print "a and b has different identity"  # a and b has different identity
else:
    print "a and b has the same identity"


# Operator priority
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print e  # 90

e = ((a + b) * c) / d
print e  # 90

e = (a + b) * (c / d)
print e  # 90

e = a + (b * c) / d
print e  # 50


