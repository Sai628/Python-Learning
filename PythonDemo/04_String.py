# coding=utf8

var1 = 'Hello World!'
var2 = "Python Language"

print "var1[0]:", var1[0]  # var1[0]: H
print "var2[1:5]", var2[1:5]  # var2[1:5] ytho


# Operator
a = "Hello"
b = "Python"

print "a+b:", a + b  # a+b: HelloPython
print "a*2:", a * 2  # a*2: HelloHello
print "a[1]:", a[1]  # a[1]: e
print "a[1:4]:", a[1:4]  # a[1:4]: ell

if "H" in a:
    print "H in a"  # H in a
else:
    print "H not in a"

if "M" not in a:
    print "M not in a"  # M not in a
else:
    print "M in a"


print r'\n'  # \n
print R'\n'  # \n


# Formatter
print "My name is %s and weight is %d kg!" % ('Zara', 21)  # My name is Zara and weight is 21 kg!


# Triple quotes
hi = '''hi
there'''

print hi
# hi
# there


# Unicode
hello = u'Hello\u0020World!'
print hello  # Hello World!


