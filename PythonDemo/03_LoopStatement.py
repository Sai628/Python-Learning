# coding=utf-8

# while loop
count = 0
while count < 5:
    print 'The count is:', count
    count += 1
# The count is: 0
# The count is: 1
# The count is: 2
# The count is: 3
# The count is: 4

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i
# 2
# 4
# 6
# 8
# 10

i = 1
while 1:
    print i
    i += 1
    if i > 5:
        break
# 1
# 2
# 3
# 4
# 5


# while...else
count = 0
while count < 5:
    print count, 'is less than 5'
    count += 1
else:
    print count, 'is not less than 5'
# 0 is less than 5
# 1 is less than 5
# 2 is less than 5
# 3 is less than 5
# 4 is less than 5
# 5 is not less than 5


# for loop
for letter in 'python':
    print 'current letter:', letter
# current letter: p
# current letter: y
# current letter: t
# current letter: h
# current letter: o
# current letter: n

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print 'current fruit:', fruit
# current fruit: banana
# current fruit: apple
# current fruit: mango

for index in range(len(fruits)):
    print 'current fruit:', fruits[index]
# current fruit: banana
# current fruit: apple
# current fruit: mango


# for...else
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d = %d * %d' % (num, i, j)
            break
    else:
        print num, 'is a prime number'
# 10 = 2 * 5
# 11 is a prime number
# 12 = 2 * 6
# 13 is a prime number
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 2 * 8
# 17 is a prime number
# 18 = 2 * 9
# 19 is a prime number


# nested loop
i = 2
while i < 20:
    j = 2
    while j <= (i / j):
        if not(i % j):
            break
        j += 1

    if j > (i / j):
        print i, "is a prime number"

    i += 1
# 2 is a prime number
# 3 is a prime number
# 5 is a prime number
# 7 is a prime number
# 11 is a prime number
# 13 is a prime number
# 17 is a prime number
# 19 is a prime number


# break statement
for letter in 'python':
    if letter == 'h':
        break
    print 'current letter:', letter
# current letter: p
# current letter: y
# current letter: t

var = 10
while var > 0:
    print 'current variable value:', var
    var -= 1
    if var == 5:
        break
# current variable value: 10
# current variable value: 9
# current variable value: 8
# current variable value: 7
# current variable value: 6


# continue statement
for letter in 'python':
    if letter == 'h':
        continue
    print 'current letter:', letter
# current letter: p
# current letter: y
# current letter: t
# current letter: o
# current letter: n

var = 5
while var > 0:
    var -= 1
    if var == 3:
        continue
    print 'current variable value:', var
# current variable value: 4
# current variable value: 2
# current variable value: 1
# current variable value: 0


# pass statement
for letter in 'python':
    if letter == 'h':
        pass
        print 'this is pass block'
    print 'current letter:', letter
# current letter: p
# current letter: y
# current letter: t
# this is pass block
# current letter: h
# current letter: o
# current letter: n
