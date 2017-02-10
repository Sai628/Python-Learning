# coding=utf-8


# Try
try:
    fh = open("testfile", 'w')
    fh.write("this is a test, just for test Exception!")
except IOError:
    print "Error: not found file or read file failure"
else:
    print "write content into file successful!"  # write content into file successful!
    fh.close()


# Try-Finally
try:
    fh = open("testfile", 'w')
    try:
        fh.write("this is a test, just for test Exception!")
    finally:
        print "close file"  # close file
        fh.close()
except IOError:
    print "Error: not found file or read file failure"


# Exception Argument
def temp_covert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "Argument no contains number:", Argument  # Argument no contains number: invalid literal for int() with base 10: 'xyz'

temp_covert("xyz")


# Raise Exception
def myexception(level):
    if level < 1:
        raise Exception("Invalid level!", level)

try:
    myexception(0)
except Exception, Argument:
    print 1, Argument  # 1 ('Invalid level!', 0)
else:
    print 2


# Custom Exception
class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise NetworkError("Bad hostname")
except NetworkError, e:
    print e.args  # ('B', 'a', 'd', ' ', 'h', 'o', 's', 't', 'n', 'a', 'm', 'e')
