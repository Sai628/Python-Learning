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


# String Build-in Functions

# Function - count
str1 = "this is string example....wow!!!"
print str1.capitalize()  # This is string example....wow!!!
print str1.center(40, 'a')  # aaaathis is string example....wow!!!aaaa
print str1.count('i', 4, 40)  # 2
print str1.count('i')  # 3
print str1.count("wow")  # 1


# Function - encode
str1 = str1.encode('base64', 'strict')
print str1
# dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=
#


# Function - decode
str1 = str1.decode('base64', 'strict')
print str1
# this is string example....wow!!!


# Function - endswith
suffix = "wow!!!"
print str1.endswith(suffix)  # True
print str1.endswith(suffix, 20)  # True

suffix = "is"
print str1.endswith(suffix, 2, 4)  # True
print str1.endswith(suffix, 2, 6)  # False


# Function - expandtabs
str1 = "this is\tstring example....wow!!!"
print str1
print str1.expandtabs()
print str1.expandtabs(16)
# this is	string example....wow!!!
# this is string example....wow!!!
# this is         string example....wow!!!


# Function - find
str1 = "this is string example....wow!!!"
str2 = "exam"
print str1.find(str2)  # 15
print str1.find(str2, 10)  # 15
print str1.find(str2, 40)  # -1
