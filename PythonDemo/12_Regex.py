# coding=utf-8


import re


# re.match
print (re.match('www', 'www.google.com').span())  # (0, 3)
print (re.match('com', 'www.google.com'))  # None


line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group():", matchObj.group()  # matchObj.group(): Cats are smarter than dogs
    print "matchObj.group(1):", matchObj.group(1)  # matchObj.group(1): Cats
    print "matchObj.group(2):", matchObj.group(2)  # matchObj.group(2): smarter
    print "matchObj.groups():", matchObj.groups()  # matchObj.groups(): ('Cats', 'smarter')
else:
    print "No match."


# re.search
print (re.search('www', 'www.google.com').span())  # (0, 3)
print (re.search('com', 'www.google.com').span())  # (11, 14)


line2 = "Cats are smart than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line2, re.M | re.I)
if searchObj:
    print "searchObj.group():", searchObj.group()  # searchObj.group(): Cats are smart than dogs
    print "searchObj.group(1):", searchObj.group(1)  # searchObj.group(1): Cats
    print "searchObj.group(2)", searchObj.group(2)  # searchObj.group(2) smart
    print "searchObj.groups()", searchObj.groups()  # searchObj.groups() ('Cats', 'smart')
else:
    print "Nothing found!"


# re.sub
phone = "2004-959-959 # this is a comment in phone"
num = re.sub(r'#.*$', "", phone)
print "the phone number:", num  # the phone number: 2004-959-959

num = re.sub(r'\D', "", phone)
print "the phone number:", num  # the phone number: 2004959959


def double(matched):
    value = int(matched.group("value"))
    return str(value * 2)

s = 'A23G4HFD567'
print (re.sub('(?P<value>\d+)', double, s))  # A46G8HFD1134
