# coding=utf-8


# Call
def printme(text):
    print text
    return

printme("I will call a custom function")  # I will call a custom function
printme("Call the same function again")  # Call the same function again


# Reference Parameter
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print "Value in function:", mylist  # Value in function: [10, 20, 30, [1, 2, 3, 4]]
    return

mylist = [10, 20, 30]
changeme(mylist)
print "Value out function:", mylist  # Value out function: [10, 20, 30, [1, 2, 3, 4]]


# Keyword Parameter
def printinfo(name, age):
    print "Name:", name
    print "Age:", age
    return

printinfo(age=50, name="miki")
'''
Name: miki
Age: 50
'''


# Default Parameters
def printinfo2(name, age=35):
    print "Name:", name
    print "Age:", age
    return

printinfo2(age=50, name="miki")
'''
Name: miki
Age: 50
'''

printinfo2("miki")
'''
Name: miki
Age: 35
'''


# Variable Length Parameters
def printinfo3(arg1, *vartuple):
    print "Output:"
    print arg1
    for var in vartuple:
        print var
    return

printinfo3(10)
'''
Output:
10
'''

printinfo3(100, 200, 300)
'''
Output:
100
200
300
'''


# Anonymous Function - Lambda
sum = lambda arg1, arg2: arg1 + arg2
print sum(10, 20)  # 30
print sum(30, 50)  # 80


# Return Statement
def sum2(arg1, arg2):
    total = arg1 + arg2
    return total

print sum2(10, 30)  # 40


# Variable Scope
total = 0

def sum3(arg1, arg2):
    total = arg1 + arg2
    print "Value in function:", total
    return total

sum3(12, 34)  # Value in function: 46
print "Value out function:", total  # Value out function: 0
