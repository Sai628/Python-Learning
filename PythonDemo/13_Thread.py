# coding=utf-8


import thread
import threading
import Queue
import time

# start thread
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (thread_name, time.ctime())


'''
try:
    thread.start_new_thread(print_time, ("Thread-1", 2))
    thread.start_new_thread(print_time, ("Thread-2", 4))
except:
    print "Error: unable to start thread"
'''


# when test the thread code above, should remove the comment of the following code.
# while 1:
#     pass

'''
Thread-1: Thu Nov 10 11:28:43 2016
Thread-2: Thu Nov 10 11:28:45 2016
Thread-1: Thu Nov 10 11:28:45 2016
Thread-1: Thu Nov 10 11:28:47 2016
Thread-2: Thu Nov 10 11:28:49 2016
Thread-1: Thu Nov 10 11:28:49 2016
Thread-1: Thu Nov 10 11:28:51 2016
Thread-2: Thu Nov 10 11:28:53 2016
Thread-2: Thu Nov 10 11:28:57 2016
Thread-2: Thu Nov 10 11:29:01 2016
'''


# thread module
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        print "Starting %s" % self.name
        print_time(self.name, self.counter)
        print "Exiting %s" % self.name


thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# when test the thread code above, should remove the comment of the following code.
# thread1.start()
# thread2.start()

# print "Exiting Main Thread"

'''
Starting Thread-1
Starting Thread-2
Exiting Main Thread
Thread-1: Thu Nov 10 11:55:07 2016
Thread-2: Thu Nov 10 11:55:08 2016
Thread-1: Thu Nov 10 11:55:08 2016
Thread-1: Thu Nov 10 11:55:09 2016
Thread-2: Thu Nov 10 11:55:10 2016
Thread-1: Thu Nov 10 11:55:10 2016
Thread-1: Thu Nov 10 11:55:11 2016
Exiting Thread-1
Thread-2: Thu Nov 10 11:55:12 2016
Thread-2: Thu Nov 10 11:55:14 2016
Thread-2: Thu Nov 10 11:55:16 2016
Exiting Thread-2
'''


# thread synchronous
class MyThread2(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        print "Start %s" % self.name
        threadLock.acquire()
        print_time(self.name, self.counter)
        threadLock.release()


threadLock = threading.Lock()
threads = []

thread1 = MyThread2(1, "Thread2-1", 1)
thread2 = MyThread2(2, "Thread2-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

'''
Start Thread2-1
Start Thread2-2
Thread2-1: Thu Nov 10 12:53:08 2016
Thread2-1: Thu Nov 10 12:53:09 2016
Thread2-1: Thu Nov 10 12:53:10 2016
Thread2-1: Thu Nov 10 12:53:11 2016
Thread2-1: Thu Nov 10 12:53:12 2016
Thread2-2: Thu Nov 10 12:53:14 2016
Thread2-2: Thu Nov 10 12:53:16 2016
Thread2-2: Thu Nov 10 12:53:18 2016
Thread2-2: Thu Nov 10 12:53:20 2016
Thread2-2: Thu Nov 10 12:53:22 2016
'''

print "Exiting Main Thread"  # Exiting Main Thread


# thread Queue
class MyThread3(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q


    def run(self):
        print "Starting %s" % self.name
        process_data(self.name, self.q)
        print "Exiting %s" % self.name


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)


exitFlag = 0
threadList = ['Thread3-1', 'Thread3-2', 'Thread3-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
    t = MyThread3(threadID, tName, workQueue)
    t.start()
    threads.append(t)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

'''
Starting Thread3-1
Starting Thread3-2
Starting Thread3-3
Thread3-3 processing One
Thread3-1 processing Two
Thread3-2 processing Three
Thread3-3 processing Four
Thread3-1 processing Five
Exiting Thread3-3
Exiting Thread3-1
Exiting Thread3-2
'''

print "Exiting Main Thread"  # Exiting Main Thread
