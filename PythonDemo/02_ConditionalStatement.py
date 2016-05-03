# coding=utf-8

flag = False
name = 'luren'
if name == 'python':
    flag = True
    print 'welcome boss'
else:
    print name  # luren


num = 5
if num == 3:
    print 'boss'
elif num == 2:
    print "user"
elif num == 1:
    print 'worker'
elif num < 0:
    print 'error'
else:
    print 'roadman'  # roadman


num = 9
if num >= 0 and num <= 10:
    print 'hello'  # hello


num = 10
if num < 0 or num > 10:
    print 'hello'
else:
    print 'undefine'  # undefine


num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'  # undefine
