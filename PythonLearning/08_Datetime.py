# coding=utf-8


import time
import calendar


# Time
ticks = time.time()
print "now timestamp is:", ticks  # now timestamp is: 1478518118.77

localtime = time.localtime(ticks)
print "local time is:", localtime  # local time is: time.struct_time(tm_year=2016, tm_mon=11, tm_mday=7, tm_hour=19, tm_min=30, tm_sec=30, tm_wday=0, tm_yday=312, tm_isdst=0)
print localtime.tm_year  # 2016
print localtime.tm_mon  # 11


# Format Datetime
localtime = time.asctime(time.localtime(time.time()))
print "local time is:", localtime  # local time is: Mon Nov  7 19:34:34 2016

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 2016-11-07 19:36:39
print time.strftime("%a %b %d %H:%M:%S", time.localtime())  # Mon Nov 07 19:37:17

a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))  # 1459175064.0


# Calendar
cal = calendar.month(2016, 1)
print "the calendar of 2016-01 is:"  # the calendar of 2016-01 is:
print cal

'''
    January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
'''


# Time Build-in Functions
# Function - altzone
print "time.altzone %d" % time.altzone  # time.altzone -28800


# Function - asctime
t = time.localtime()
print "time.asctime(t): %s" % time.asctime(t)  # time.asctime(t): Mon Nov  7 20:08:16 2016


# Function - clock
def procedure():
    time.sleep(2.5)

t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"  # 5.1e-05 seconds process time

t0 = time.time()
procedure()
print time.time() - t0, "seconds process time"  # 2.50480413437 seconds process time


# Function - ctime
print "time.ctime(): %s" % time.ctime()  # time.ctime(): Mon Nov  7 20:21:56 2016


# Function - gmtime
print "time.gmtime(): %s" % time.gmtime()  # time.gmtime(): time.struct_time(tm_year=2016, tm_mon=11, tm_mday=7, tm_hour=12, tm_min=23, tm_sec=49, tm_wday=0, tm_yday=312, tm_isdst=0)


# Function - localtime
print "time.localtime(): %s" % time.localtime()  # time.localtime(): time.struct_time(tm_year=2016, tm_mon=11, tm_mday=7, tm_hour=20, tm_min=29, tm_sec=28, tm_wday=0, tm_yday=312, tm_isdst=0)


# Function - mktime
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)
print "time.mktime(t): %f" % secs  # time.mktime(t): 1234861418.000000
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))  # asctime(localtime(secs)): Tue Feb 17 17:03:38 2009


# Function - sleep
print "Start: %s" % time.ctime()  # Start: Mon Nov  7 20:34:23 2016
time.sleep(2)
print "End: %s" % time.ctime()  # End: Mon Nov  7 20:34:25 2016


# Function - strftime
t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))  # Feb 17 2009 09:03:38


# Function - strptime
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print "return tuple: %s" % struct_time  # return tuple: time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)


# Function - time
print "time.time(): %f" % time.time()  # time.time(): 1478527494.642500
print time.localtime(time.time())  # time.struct_time(tm_year=2016, tm_mon=11, tm_mday=7, tm_hour=22, tm_min=4, tm_sec=54, tm_wday=0, tm_yday=312, tm_isdst=0)
print time.asctime(time.localtime(time.time()))  # Mon Nov  7 22:04:54 2016
